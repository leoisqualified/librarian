from django.contrib import admin
from .models import Books, Member, BorrowingRecord

# Register your models here.
admin.site.register(Books)
admin.site.register(Member)
admin.site.register(BorrowingRecord)