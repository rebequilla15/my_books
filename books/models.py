from django.db import models

<<<<<<< HEAD
# Create your models here.
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

=======
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
>>>>>>> f50c3fbfa3bde008fa8ebd909ddcdb64451d3bc7

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    image = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
=======
    update_at = models.DateTimeField(auto_now=True)  # Se actualiza automáticamente en cada modificación
>>>>>>> f50c3fbfa3bde008fa8ebd909ddcdb64451d3bc7

    def __str__(self):
        return self.title