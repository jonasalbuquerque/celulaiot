from django.db import models

class Noticia(models.Model):
    ativo = models.BooleanField()

class Message(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()
