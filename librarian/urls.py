from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('material-types/', views.material_type_list, name='material_type_list'),
    path('material-types/add/', views.add_material_type, name='add_material_type'),
    path('material-types/edit/<int:material_type_id>/', views.edit_material_type, name='edit_material_type'),
    path('material-types/delete/<int:material_type_id>/', views.delete_material_type, name='delete_material_type'),
]