from django.shortcuts import render

from django.http import HttpResponse

from .forms import MessageForm


def index(request):
    return render(request, 'noticias/index.html', {})

def apresentacao(request):
	return render(request, 'noticias/apresentacao.html', {})

def cursos(request):
	return render(request, 'noticias/cursos.html', {})

def projetos(request):
	return render(request, 'noticias/projetos.html', {})
