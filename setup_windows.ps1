# Verificar se o Python está instalado, caso contrário, tentar instalar
$pythonPath = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonPath) {
    Write-Host "Python não encontrado. Instale o Python manualmente."
    exit
}

# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
& ".\venv\Scripts\Activate.ps1"

# Instalar as dependências a partir do arquivo requirements.txt
pip install -r requirements.txt

Write-Host "Ambiente configurado e dependências instaladas."
