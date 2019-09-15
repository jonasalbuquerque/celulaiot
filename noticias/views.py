from django.shortcuts import render

from django.http import HttpResponse

from .forms import MessageForm


def index(request):
    return render(request, 'noticias/index.html', {})

def apresentacao(request):
	return render(request, 'noticias/soon.html', {})

def cursos(request):
	return render(request, 'noticias/soon.html', {})

def projetos(request):
	return render(request, 'noticias/soon.html', {})
