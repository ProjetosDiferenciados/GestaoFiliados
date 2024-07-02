# Adiciona o Poetry ao PATH do sistema para a sessão atual
$env:Path += ";$($env:USERPROFILE)\.local\bin"

# Executa o comando do Poetry
poetry run gestao_filiados/manage.py runserver