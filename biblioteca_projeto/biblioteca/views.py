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
