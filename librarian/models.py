from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    category = models.CharField(max_length=100)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    
    def __str__(self):
        return self.title
    

#  Member Table
class Member(models.Model):
    name = models.OneToOneField(User, max_length=100, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    membership_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
# Borrowing
class BorrowingRecord(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    due_date = models.DateField()
    
    def __str__(self):
        return f"{self.member.user.username} borrowed {self.book.title}"


