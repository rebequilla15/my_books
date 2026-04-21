<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('detail_book/<int:id>/', views.detail_book, name='detail_book'),
=======
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),  # Incluye las URLs de la aplicación books
>>>>>>> f50c3fbfa3bde008fa8ebd909ddcdb64451d3bc7
]