#!/bin/bash

# Atualiza a lista de pacotes e instala as dependências necessárias
sudo apt update
sudo apt install -y curl python3 python3-pip

# Baixa o script de instalação do Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Adiciona Poetry ao PATH
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Verifica a instalação do Poetry
poetry --version
# Aguarda o usuário pressionar Enter antes de finalizar
echo "# INSTALAÇÃO FINALIZADA Pressione Enter para finalizar..."
read