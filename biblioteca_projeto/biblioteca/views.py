from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Livro

class LivroListView(ListView):
    model = Livro
    template_name = 'livro_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Livro.objects.filter(categoria__icontains=query)
        return Livro.objects.all()

class LivroCreateView(LoginRequiredMixin, CreateView):
    model = Livro
    fields = ['titulo', 'autor', 'categoria', 'descricao', 'capa']
    template_name = 'livro_form.html'
    success_url = reverse_lazy('livro_list')

class LivroUpdateView(LoginRequiredMixin, UpdateView):
    model = Livro
    fields = ['titulo', 'autor', 'categoria', 'descricao', 'capa']
    template_name = 'livro_form.html'
    success_url = reverse_lazy('livro_list')

class LivroDeleteView(LoginRequiredMixin, DeleteView):
    model = Livro
    template_name = 'livro_confirm_delete.html'
    success_url = reverse_lazy('livro_list')    

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Livro
from .forms import LivroForm

@login_required
def criar_livro(request):
    if request.method == 'POST':
        # IMPORTANTE: request.FILES é obrigatório para receber imagens!
        form = LivroForm(request.POST, request.FILES)
        if form.is_dict() if hasattr(form, 'is_dict') else form.is_valid():
            livro = form.save(commit=False)
            livro.usuario = request.user # Associa o livro ao usuário logado
            livro.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/criar_livro.html', {'form': form})

@login_required
def listar_livros(request):
    livros = Livro.objects.filter(usuario=request.user)
    
    # Filtros por Busca (Título/Autor) e por Gênero
    busca = request.GET.get('busca')
    genero = request.GET.get('genero')

    if busca:
        livros = livros.filter(Q(titulo__icontains=busca) | Q(autor__icontains=busca))
    if genero:
        livros = livros.filter(genero=genero)

    context = {
        'livros': livros,
        'generos': Livro.GENEROS,
    }
    return render(request, 'livros/listar_livros.html', context)