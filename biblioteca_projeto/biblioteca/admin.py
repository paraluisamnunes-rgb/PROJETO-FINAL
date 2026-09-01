from django.contrib import admin
from .models import Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'ano_publicacao', 'usuario', 'data_cadastro')
    list_filter = ('genero', 'ano_publicacao', 'data_cadastro')
    search_fields = ('titulo', 'autor', 'resumo')
    ordering = ('-data_cadastro',)
    list_per_page = 20

# Personalizando títulos do painel Django Admin
admin.site.site_header = "Administração da Biblioteca Pessoal"
admin.site.site_title = "Painel Biblioteca"
admin.site.index_title = "Gerenciamento de Acervo"