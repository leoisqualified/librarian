from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, MaterialType
from .forms import BookForm, MaterialTypeForm

# Create your views here.
# Display all the books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'librarian/book_list.html', {'books': books})

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
    return render(request, 'librarian/add_book.html', {'form': form})

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
    return render(request, 'librarian/edit_book.html', {'form': form, 'book': book})


# Delete a Book
def delete_book(request, book_id):
    book = get_object_or_404(Book, book_id)
    if request.method =='POST':
        form = BookForm(instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book_id)
    return render(request, 'librarian/delete_book.html', {'form':form, 'book': book})


        
