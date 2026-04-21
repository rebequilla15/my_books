
from django.contrib import admin
from django.urls import path
from .views import home, detail

urlapatterns = [
    path ('',home,name='home'), 
    path('books/<int:id>/', detail,name='post_detail'),
]





