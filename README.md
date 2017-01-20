# Projeto Base

Projeto Base

## Como desenvolver ?

1. Clone o repositório.
2. Crie um virutalenv com o Python 3.5
3. Ative o Virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env
6. Roda o collectstatic para configurar arquivos staticos
7. Execute os testes.

```console
git clone 
cd 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py collectstatic
python manage.py test
python manage.py runserver
```

## Como fazer deploy ?


**NOTES**

