from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def index(request):
    query = request.GET.get("q")

    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all().order_by("title")

    return render(request, "library/index.html", {"books": books})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = BookForm()

    return render(request, "library/add_book.html", {"form": form})

def edit_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = BookForm(instance=book)

    return render(request, "library/edit_book.html", {"form": form})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("index")