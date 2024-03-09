from django.urls import path
from Libreria.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', start, name='start'),
    path('nosotros/', us, name='us'),
    path('libros/', list_books, name='list_books'),
    path('libros/crear/', create_book, name='create_book'),
    path('libros/editar/', edit_book, name='edit_book')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)