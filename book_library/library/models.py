from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=[("available", "Available"), ("borrowed", "Borrowed")], default="available")

    def __str__(self):
        return self.title

class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrowings")
    borrower_name = models.CharField(max_length=255)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.returned_at:
            self.book.status = "borrowed"
        else:
            self.book.status = "available"
        self.book.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.borrower_name} borrowed {self.book.title}"
