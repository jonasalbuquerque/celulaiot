from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'noticias/index.html', {})

def generic(request):
	return render(request, 'noticias/generic.html', {})
