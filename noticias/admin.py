from django.contrib import admin
from .models import Noticia


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('nome')
   
admin.site.register(Noticia)