from django.urls import path
from Libreria.views import *


urlpatterns = [
    path('', start, name='start'),
    path('nosotros/', us, name='us'),
    path('libros/', list_books, name='list_books'),
    path('libros/crear/', create_book, name='create_book')
]