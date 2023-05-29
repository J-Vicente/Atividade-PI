from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('lista_locacao/',locacao,name='locacao'),
    path('lista_filmes/',filmes,name='filmes'),
]