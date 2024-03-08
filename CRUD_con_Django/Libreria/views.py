from django.shortcuts import render
from django.http import HttpResponse


def start(request):
    return render(request, 'index.html')


def us(request):
    return render(request, 'us.html')


def list_books(request):
    return render(request, 'books/list_books.html')


def create_book(request):
    return render(request, 'books/create_book.html')

def edit_book(request):
    return render(request, 'books/edit_book.html')