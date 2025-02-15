from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Borrowing
from .forms import BorrowingForm, BookForm
from django.utils.timezone import now

def book_list(request):
    books = Book.objects.all()
    return render(request, "library/book_list.html", {"books": books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "library/book_details.html", {"book": book})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "library/add_book.html", {"form": form})

def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.status == "borrowed":
        return redirect("book_list")

    if request.method == "POST":
        form = BorrowingForm(request.POST)
        if form.is_valid():
            borrowing = form.save(commit=False)
            borrowing.book = book
            borrowing.save()
            return redirect("book_detail", book_id=book.id)
    else:
        form = BorrowingForm()
    return render(request, "library/borrow_book.html", {"form": form, "book": book})

def return_book(request, borrowing_id):
    borrowing = get_object_or_404(Borrowing, id=borrowing_id)
    borrowing.returned_at = now()
    borrowing.save()
    return redirect("book_detail", book_id=borrowing.book.id)
