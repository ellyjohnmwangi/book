from django import forms
from .models import Borrowing, Book

class BorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ["borrower_name"]

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]
