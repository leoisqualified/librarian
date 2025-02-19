from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def Books():
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    category = models.CharField(max_length=100)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    
    def __str__(self):
        return self.title
    

#  Member Table
def Member():
    name = models.OneToOneField(User, max_length=100)
    phone = models.CharField(max_length=15)
    membership_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
# Borrow model
def borrow():
    borrower_name = models.CharField(max_length=100)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    
    def __str__(self):
        return self.borrower_name