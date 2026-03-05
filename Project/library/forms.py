from django import forms
from django.utils import timezone
from .models import Book
from .models import Borrowing, Person

class BorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ["person"]

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]

    def clean_publication_year(self):
        year = self.cleaned_data["publication_year"]
        current_year = timezone.now().year

        if year > current_year:
            raise forms.ValidationError("Rok wydania nie może być w przyszłości.")
        if year < 1000:
            raise forms.ValidationError("Rok wydania wygląda na niepoprawny (min. 1000).")

        return year