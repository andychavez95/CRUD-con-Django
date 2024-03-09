from django.shortcuts import render, redirect
from Libreria.models import Books
from Libreria.forms import BooksForm

def start(request):
    return render(request, 'index.html')


def us(request):
    return render(request, 'us.html')


def list_books(request):
    # Obtenemos todos los libros de la tabla Books.
    all_books = Books.objects.all()
    return render(request, 'books/list_books.html', {'books': all_books})


def create_book(request):
    books_form = BooksForm(request.POST or None, request.FILES or None)
    if books_form.is_valid():
        books_form.save()
        return redirect(list_books)
    return render(request, 'books/create_book.html', {'form': books_form})

def edit_book(request):
    return render(request, 'books/edit_book.html')