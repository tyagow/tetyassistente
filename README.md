# Tety Assistente

[![CircleCI](https://circleci.com/gh/tyagow/tetyassistente.svg?style=svg)](https://circleci.com/gh/tyagow/tetyassistente) [![Coverage Status](https://coveralls.io/repos/github/tyagow/tetyassistente/badge.svg?branch=master)](https://coveralls.io/github/tyagow/tetyassistente?branch=master)



## Como desenvolver ?

TODO: Adicionar como instalar redis e rodar o celery localmente para funcionar o scrap localmente tambem


1. Clone o repositório.
2. Crie um virutalenv com o Python 3.6.1
3. Ative o Virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env
6. Migre seus modelos para o Banco de Dados
7. Execute os testes.
8. Roda o servidor

```console
git clone https://github.com/tyago/tetyassistente.git tetyassistente 
cd tetyassistente
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py migrate
python manage.py test
python manage.py runserver
```

## Como fazer deploy ?

TODO


## dokku help      
Usage: dokku [--quiet|--trace|--rm-container|--rm|--force] COMMAND <app> [command-specific-options]

Primary help options, type "dokku COMMAND:help" for more details, or dokku help --all to see all commands.

Commands:

    apps             List your apps
    certs            Manage Dokku apps SSL (TLS) certs
    checks           Show zero-downtime status
    config           Display all global or app-specific config vars
    docker-options   Display app's Docker options for all phases (or comma separated phase list)
    domains          List domains
    enter            Connect to a specific app container
    events           Show the last events (-t follows)
    help             Print the list of commands
    logs             Show the last logs for an application
    ls               Pretty listing of deployed applications and containers
    nginx            Interact with Dokku's Nginx proxy
    plugin           Print active plugins
    proxy            Show proxy settings for app
    ps               List processes running in app container(s)
    run              Run a command in the environment of an application
    shell            Spawn dokku shell
    ssh-keys         Manage public ssh keys that are allowed to connect to Dokku
    storage          Mount local volume / directories inside containers
    tags             List all app image tags
    trace            Enable dokku tracing
    url              Show the first URL for an application (compatibility)
    urls             Show all URLs for an application
    version          Print dokku's version

Community plugin commands:

    postgres   Plugin for managing Postgres services
    redis      Plugin for managing Redis services



TODO
-----

* [ ] In report List - Each row has respective color as the type of the report 
* [ ] In report List - Table with reports must have type column 
* [ ] In Report Form - Align title center
* [ ] Report type FEELING  must have some kind score and/or thumbs up/down
* [ ] Report time possible timezone divergence - must use Local timezone
