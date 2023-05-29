from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=(100))

class Filme(models.Model):
    titulo = models.CharField(max_length=(150))
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

class Cliente(models.Model):
    nome = models.CharField(max_length=(100))
    email = models.EmailField()

class Locacao(models.Model):
    nome = models.CharField(max_length=(100))
    data = models.DateField() 
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    filme = models.ManyToManyField(Filme)

