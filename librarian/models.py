from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MaterialType(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    subject = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    publisher = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    material_type = models.ForeignKey(MaterialType, on_delete=models.CASCADE)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    

#  Member Table
class Member(models.Model):
    name = models.OneToOneField(User, max_length=100, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255, default="Unknown")
    membership_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user.get_full_username()
    
class BorrowingRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    due_date = models.DateField()
    fine = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calculate_fine(self):
        if self.return_date and self.return_date > self.due_date:
            days_overdue = (self.return_date - self.due_date).days
            self.fine = days_overdue * 1.00
        else:
            self.fine = 0.00
        self.save()

    def __str__(self):
        return f"{self.member.user.username} borrowed {self.book.title}"
    
class Hold(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    hold_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.user.username} placed a hold {self.book.title}"


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Acquisition(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str___(self):
        return f"Order for {self.book.title} from {self.vendor.name}"


