from django.db import models

class Noticia(models.Model):
    ativo = models.BooleanField()
