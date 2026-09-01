# PROJETO-FINAL
Projeto Final da U.C. 3 do curso de Python
Python
readme_content = """# Sistema de Gerenciamento de Biblioteca Pessoal (Livros)

Este projeto consiste em uma aplicação web desenvolvida em **Python** utilizando o framework **Django**. O sistema permite gerenciar uma biblioteca pessoal de livros, contando com fluxo completo de C.R.U.D., autenticação de usuários, upload de capas de livros e interface responsiva construída com Bootstrap.

---

## 📋 Funcionalidades Otimizadas

- **Autenticação:** Login e Logout de usuários integrados ao sistema nativo do Django.
- **C.R.U.D. Completo:**
  - **Create:** Cadastro de novos livros com título, autor, categoria, descrição e imagem de capa.
  - **Read:** Listagem geral de livros com filtro por categoria/título.
  - **Update:** Edição de dados e upload de nova capa para livros existentes.
  - **Delete:** Remoção de livros do acervo.
- **Upload de Arquivos:** Suporte a arquivos de imagem para a capa dos livros (`media/capas`).
- **Área Administrativa Customizada:** Listagem com colunas personalizadas e busca configurada no painel Admin do Django.
- **Interface Responsiva:** Construída com a estrutura de templates do Django (`base.html` + componentes) e estilizada via Bootstrap 5.

---

## 🛠️ Tecnologias Utilizadas

- **Back-end:** Python 3.x, Django 4.x
- **Front-end:** HTML5, CSS3 (Bootstrap 5 via CDN)
- **Banco de Dados:** SQLite (padrão de desenvolvimento)
- **Ambiente de Desenvolvimento:** `venv` (Ambiente Virtual Python)

---

## 📂 Estrutura do Projeto

```text
meu_projeto/
├── biblioteca/             # Aplicação Principal
│   ├── migrations/
│   ├── static/             # Arquivos estáticos (CSS, JS, Imagens)
│   ├── templates/          # Templates específicos da app
│   │   └── livros/
│   │       ├── livro_list.html
│   │       ├── livro_form.html
│   │       └── livro_confirm_delete.html
│   ├── admin.py            # Personalização do Painel de Admin
│   ├── models.py           # Model de Dados (Livro)
│   ├── urls.py             # Rotas do app
│   └── views.py            # Logic (Class-Based Views)
├── meu_projeto/            # Configuração Global do Projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/                  # Uploads de imagens (Capas)
├── templates/              # Templates globais
│   ├── base.html           # Template base
│   ├── componentes/        # Partial templates (navbar, etc.)
│   └── registration/       # Templates de login/logout
│       └── login.html
├── manage.py
├── requirements.txt
└── README.md


