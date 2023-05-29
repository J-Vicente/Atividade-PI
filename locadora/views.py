from django.shortcuts import render
from django.http import HttpResponse
from .models import Locacao, Filme

# Create your views here.

def index(request):
    return render(request,"index.html")

def locacao(request):
    context = Locacao.objects.all()
    # context = {'nome': Locacao.nome, 'data':Locacao.data, 'cliente':Locacao.cliente, 'filme':Locacao.filme}
    return render(request,"locacao.html",context)

def filmes(request):
    context = {'nome': Filme.titulo, 'valor': Filme.valor, 'categoria': Filme.categoria}
    return render(request,"filmes.html",context)