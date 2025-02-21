from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, MaterialType
from .forms import BookForm, MaterialTypeForm

# Create your views here.
# Display all the books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Adding a book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.available_copies = book.total_copies
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# Edit a book
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})


# Delete a Book
def delete_book(request, book_id):
    book = get_object_or_404(Book, book_id)
    book.delete()
    return redirect('book_list')


# Material Type View

#Display all material
def material_type_list(request):
    material_types = MaterialType.objects.all()
    return render(request, 'material_type_list.html', {'material_types': material_types}) 

# Add a material type
def add_material_type(request):
    if request.method == 'POST':
        form = MaterialTypeForm(request.POST)
        if form.is_valid():
            material_type = form.save(commit=False)
            material_type.save()
            return redirect('material_type_list')
    else:
        form = MaterialTypeForm()
    return render(request, 'add_material_type.html', {'form': form})

# Edit a Material Type
def edit_material_type(request, material_type_id):
    material_type = get_object_or_404(MaterialType, id=material_type_id)
    if request.method == 'POST':
        form = MaterialTypeForm(request.POST, instance=material_type)
        if form.is_valid():
            form.save()
            return redirect('material_type_list')
    else:
        form = MaterialTypeForm(instance=material_type)
    return render(request, 'edit_material_type.html', {'form': form,'material_type': material_type})

# Delete a Material Type
def delete_material_type(request, material_type_id):
    material_type = get_object_or_404(MaterialType, material_type_id)
    material_type.delete()
    return redirect('material_type_list')
       
