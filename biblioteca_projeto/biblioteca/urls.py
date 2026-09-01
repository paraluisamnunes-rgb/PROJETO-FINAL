from django.urls import path
from .views import LivroListView, LivroCreateView, LivroUpdateView, LivroDeleteView

urlpatterns = [
    path('', LivroListView.as_view(), name='livro_list'),
    path('novo/', LivroCreateView.as_view(), name='livro_create'),
    path('editar/<int:pk>/', LivroUpdateView.as_view(), name='livro_update'),
    path('deletar/<int:pk>/', LivroDeleteView.as_view(), name='livro_delete'),
]

from . import views

urlpatterns = [
    path('livros/', views.listar_livros, name='listar_livros'),
    path('livros/novo/', views.criar_livro, name='criar_livro'),
]