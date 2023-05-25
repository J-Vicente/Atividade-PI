from django.contrib import admin
from .models import Locacao, Cliente
# Register your models here.


@admin.register(Locacao)
class PessoaProjetoAdimin(admin.ModelAdmin):
    list_display =['nome','data']


@admin.register(Cliente)
class PessoaProjetoAdimin(admin.ModelAdmin):
    list_display =['nome','email']