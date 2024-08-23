#!/bin/bash

# Verificar se o Python está instalado, caso contrário, tentar instalar
if ! command -v python3 &> /dev/null
then
    echo "Python não encontrado. Tentando instalar..."
    brew install python3
fi

# Criar o ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate

# Instalar as dependências a partir do arquivo requirements.txt
pip install -r requirements.txt

echo "Ambiente configurado e dependências instaladas."
