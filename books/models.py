from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    image = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)  # Se actualiza automáticamente en cada modificación

    def __str__(self):
        return self.title