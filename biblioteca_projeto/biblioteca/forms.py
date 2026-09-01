from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'genero', 'ano_publicacao', 'resumo', 'capa']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'ano_publicacao': forms.NumberInput(attrs={'class': 'form-control'}),
            'resumo': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'capa': forms.FileInput(attrs={'class': 'form-control-file'}),
        }