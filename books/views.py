from django.shortcuts import render, get_object_or_404
from .models import Book

# Vista para la página de inicio
def home(request):
    books = Book.objects.all()  # Obtén todos los libros de la base de datos
    return render(request, 'books/home.html', {'books': books})

# Vista para mostrar los detalles de un libro
def detail_book(request, id):
    book = get_object_or_404(Book, id=id)  # Obtén un libro específico por su ID
    return render(request, 'books/detail_book.html', {'detail_books': book})





