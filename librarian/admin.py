from django.contrib import admin
from .models import MaterialType, Book, Member, Vendor, BorrowingRecord, Acquisition,Hold

# Register your models here.
admin.site.register(MaterialType)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Vendor)
admin.site.register(BorrowingRecord)
admin.site.register(Acquisition)
admin.site.register(Hold)