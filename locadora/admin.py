from django.contrib import admin
from .models import Locacao, Cliente, Filme, Categoria
# Register your models here.


@admin.register(Locacao)
class LocacaoProjetoAdimin(admin.ModelAdmin):
    list_display =['nome','data']


@admin.register(Cliente)
class ClienteProjetoAdimin(admin.ModelAdmin):
    list_display =['nome','email']

@admin.register(Categoria)
class CategoriaProjetoAdimin(admin.ModelAdmin):
    list_display =['nome']

@admin.register(Filme)
class FilmeProjetoAdimin(admin.ModelAdmin):
    list_display =['titulo','valor','categoria']