from django.shortcuts import render
from django.urls import path
from . import views 

# Create your views here.
urlspatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:record_id>/', views.return_book, name='return_book'),
    path('members/', views.members, name='members'),
]