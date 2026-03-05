from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.db.models import Q


def index(request):
    q = (request.GET.get("q") or "").strip()
    books = Book.objects.all()

    if q:
        books = books.filter(
            Q(title__icontains=q) |
            Q(author__name__icontains=q) |
            Q(publication_year__icontains=q)
        )

    return render(request, "library/index.html", {"books": books, "q": q})


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
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = BookForm(instance=book)

    return render(request, "library/edit_book.html", {"form": form})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.delete()
        return redirect("index")

    return render(request, "library/delete_book.html", {"book": book})