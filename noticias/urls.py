from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apresentacao', views.apresentacao, name='apresentacao'),
    path('cursos', views.cursos, name='cursos'),
    path('projetos', views.projetos, name='projetos'),
]