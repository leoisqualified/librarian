from django.urls import path
from . import views


urlspatterns = [
    path('book_list/', views.book_list, name='book_list'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:request_id>/', views.edit_book, name='edit_book'),
]