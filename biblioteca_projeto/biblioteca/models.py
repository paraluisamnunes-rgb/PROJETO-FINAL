from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    capa = models.ImageField(upload_to='capas/')

    def __str__(self):
        return self.titulo
