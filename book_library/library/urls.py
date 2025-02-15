from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:book_id>/borrow/", views.borrow_book, name="borrow_book"),
    path("borrowings/<int:borrowing_id>/return/", views.return_book, name="return_book"),
]
