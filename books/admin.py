from django.contrib import admin
from .models import Book, Category  # Importa los modelos que definiste en models.py

admin.site.register(Book)  # Registra el modelo Book para que sea accesible en el panel de administración
admin.site.register(Category)  # Registra el modelo Category para que sea accesible en el panel de administración