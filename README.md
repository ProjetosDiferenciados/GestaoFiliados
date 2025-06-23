# Projeto TSE_IMPORTADOR

Este é um projeto Python para implementação das regras de negócio de organização dos filiados de um partido político que foi desenvolvido com a ajuda do Poetry.

## Instalação

Para instalar as dependências do projeto, você pode executar o seguinte comando:

```bash
poetry install
```
## Uso
Para utilizar este pacote, basta importá-lo em seu código Python:
```python

import tse_importador

```

## Testes

Para testar e garantir a funcionalidade da biblioteca, rode através do poetry

```bash

poetry run pytest

```

## Migrar entidades

```bash

poetry run gestao_filiados/manage.py makemigrations
poetry run gestao_filiados/manage.py migrate

```

## Iniciar o django

```bash

poetry run gestao_filiados/manage.py runserver

```

A partir daí, você pode começar a utilizar as funcionalidades oferecidas pelo pacote.


## Inicializar o GUNICORN com a aplicação em django

Para inicializar o servidor web mais robusto do gunicorn,
é necessário utilizar o poetry da seguinte forma:

```bash
#primeiramente entre no pacote que contem a aplicação django
cd gestao_filiados
poetry run gunicorn gestao_filiados.wsgi:application

```


## Contribuição
Se você quiser contribuir com este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto é licenciado sob a Licença XYZ. Veja o arquivo LICENSE para mais detalhes.
