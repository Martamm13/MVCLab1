from django.contrib import admin
from .models import Author, Book, Person, Borrowing

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Person)
admin.site.register(Borrowing)