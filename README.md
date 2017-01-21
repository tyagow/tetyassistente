# Projeto Base

Projeto Base

## Como desenvolver ?

1. Clone o repositório.
2. Crie um virutalenv com o Python 3.5
3. Ative o Virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env
6. Migre seus modelos para o Banco de Dados
7. Roda o collectstatic para configurar arquivos staticos
8. Execute os testes.

```console
git clone https://github.com/tyagow/django-base.git Nome-Do-Projeto
cd 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py collectstatic
python manage.py migrate
python manage.py test
python manage.py runserver
```

## Como fazer deploy ?

* Under Contruction

## Features

* Django 1.10.5
* Bootstrap 3.3.7
* JQuery 3.1.1
* Python Decouple
* DJ Static (serving static files locally)
* Dj Database URL 
* Django test without migrations
* Django Crispy Forms
* Basic User Login App

**NOTES**

