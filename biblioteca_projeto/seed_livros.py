import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_projeto.settings') 
django.setup()

from django.contrib.auth.models import User
from biblioteca.models import Livro # Ajuste 'biblioteca' para o nome do seu app

def cadastrar_livros():
    # Obtém ou cria um usuário padrão para atribuir os livros
    usuario, _ = User.objects.get_or_create(username='admin')

    livros_dados = [
        {
            "título": "Uma mulher no escuro",
            "autor": "Raphale Montes",
            "gênero": "Suspense",
            "ano de publicação": 2019,
            "resumo": "Um crime brutal cometido há vinte anos, uma única sobrevivente, o retorno calculado do assassino."
            "Em quem Victoria deve confiar?",
        },
        {
            "título": "Animal!",
            "autor": "Domenica Luciani",
            "gênero": "Romance",
            "ano de publicação": 2007,
            "resumo": "O livro Animal!, de Domenica Luciani, narra a divertida transformação de Ozzy Baloffi, um garoto tímido de"
            "13 anos que vive em Florença e se sente um fracasso completo, mas vê sua vida virar de cabeça para baixo ao"
            "descobrir que seu pai desaparecido é, na verdade, um roqueiro famoso.",
        },
        {
            "título": "A redoma de vidro",
            "autor": "Sylvia Plath",
            "gênero": "Romance",
            "ano de publicação": 1963,
            "resumo": "Talentosa e promissora, Esther Greenwood sai do subúrbio de Boston para trabalhar em uma prestigiosa"
            "revista de moda em Nova York. No momento de transição para uma vida cheia de responsabilidades e novos desafios,"
            "Esther entra em colapso devido ao desenvolvimento de um quadro depressivo.",
        },
        {
            "título": "O Cortiço",
            "autor": "Aluísio Azevedo",
            "gênero": "Outros",
            "ano de publicação": 1890,
            "resumo": "Acompanha a vida dos moradores de uma habitação coletiva no Rio de Janeiro, destacando a influência do meio"
            "no comportamento",
        },
        {
            "titulo": "favoRita",
            "autor": "Rita Lee",
            "genero": "Autobiografia",
            "ano_publicacao": 2018,
            "resumo": "Em comemoração aos seus 70 anos, a diva do rock lança favoRita. Em uma edição especial e luxuosa, a obra"
            "apresenta textos autobiográficos e devaneios da autora.",
        }
    ]

    for dados in livros_dados:
        livro, criado = Livro.objects.get_or_create(
            titulo=dados["titulo"],
            usuario=usuario,
            defaults=dados
        )
        if criado:
            print(f"✅ Livro '{livro.titulo}' cadastrado com sucesso!")
        else:
            print(f"ℹ️ Livro '{livro.titulo}' já existia no banco.")

if __name__ == '__main__':
    cadastrar_livros()