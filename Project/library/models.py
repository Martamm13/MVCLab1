from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

    def is_borrowed(self):
      return self.borrowings.filter(returned_at__isnull=True).exists()

class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrowings")
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="borrowings")
    borrowed_at = models.DateTimeField(default=timezone.now)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.book} -> {self.person}"

    @property
    def is_active(self):
        return self.returned_at is None