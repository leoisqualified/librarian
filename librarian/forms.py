from django import forms
from .models import Book, MaterialType
                                                                      


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'author', 'isbn', 'subject', 'publication_year',
            'publisher', 'language', 'material_type', 'total_copies', 'image'
        ]
        widgets = {
            'publication_year': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
        }

class MaterialTypeForm(forms.ModelForm):
    class Meta:
        model = MaterialType
        fields = ['name']

