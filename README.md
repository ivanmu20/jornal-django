# 📰 Jornal Tech — Aplicação Django

## 📌 Descrição

O **Jornal Tech** é uma aplicação web desenvolvida em Django que simula um jornal online onde utilizadores podem visualizar artigos e interagir através de comentários.

Este projeto foi desenvolvido no âmbito de avaliação prática, com foco na utilização de **Git + GitHub**, desenvolvimento estruturado e organização de código.

---

## 🚀 Funcionalidades

* 📄 Listagem de artigos (homepage)
* 🔎 Visualização de artigo individual
* 💬 Sistema de comentários por artigo
* 🛠️ Painel de administração (Django Admin)
* 🎨 Interface moderna com Bootstrap

---

## 🧱 Tecnologias utilizadas

* **Backend:** Django (Python)
* **Frontend:** HTML + Bootstrap
* **Base de dados:** SQLite
* **Controlo de versão:** Git + GitHub

---

## 🧠 Arquitetura

Esta aplicação segue um modelo **fullstack tradicional com Django**, onde:

* O backend gere a lógica e a base de dados
* O frontend é renderizado através de templates HTML

---

## 🌐 Sobre o Firebase

O enunciado menciona o uso do Firebase para alojamento. No entanto:

* O Firebase é mais adequado para aplicações estáticas
* Django requer um servidor backend em Python

👉 Assim, o projeto pode ser alojado em plataformas como:

* Render
* Railway

O Firebase pode ser utilizado para hosting de ficheiros estáticos ou frontend separado.

---

## ⚙️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USERNAME/jornal-django.git
cd jornal-django
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
source venv/Scripts/activate
```

### 3. Instalar dependências

```bash
pip install django
```

### 4. Aplicar migrações

```bash
python manage.py migrate
```

### 5. Criar superuser

```bash
python manage.py createsuperuser
```

### 6. Executar servidor

```bash
python manage.py runserver
```

---

## 🔐 Acesso ao Admin

Aceder a:

```
http://127.0.0.1:8000/admin
```

---

## 📂 Estrutura do projeto

```
news/
├── models.py
├── views.py
├── urls.py
├── templates/

config/
├── settings.py
├── urls.py
```

---

## 📈 Possíveis melhorias

* Sistema de autenticação de utilizadores
* API com Django REST Framework
* Pesquisa de artigos
* Upload de imagens
* Deploy completo em produção

---

## 👨‍💻 Autor

Ivan Williams Mubai

---

## 📌 Nota

Este projeto demonstra conhecimentos em:

* Desenvolvimento web com Django
* Organização de código
* Utilização de Git e GitHub
* Estruturação de aplicações fullstack
