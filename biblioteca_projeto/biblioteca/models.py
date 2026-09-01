from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    GENEROS = [
        ('Romance', 'Romance'),
        ('Ficção Científica', 'Ficção Científica'),
        ('Fantasia', 'Fantasia'),
        ('Drama', 'Drama'),
        ('Outros', 'Outros'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.CharField(max_length=150, verbose_name="Autor")
    genero = models.CharField(max_length=50, choices=GENEROS, default='Outros', verbose_name="Gênero")
    ano_publicacao = models.IntegerField(verbose_name="Ano de Publicação")
    resumo = models.TextField(blank=True, null=True, verbose_name="Resumo")
    capa = models.ImageField(upload_to='capas/', blank=True, null=True, verbose_name="Capa do Livro")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="livros")
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"