from django import forms
from Libreria.models import Books

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'