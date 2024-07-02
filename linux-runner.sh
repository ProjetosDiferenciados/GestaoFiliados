#!/bin/bash

# Adiciona Poetry ao PATH para a sessão atual
export PATH="$HOME/.local/bin:$PATH"

# Executa o comando do Poetry
poetry run gestao_filiados/manage.py runserver