# Define the URL to download the Poetry installation script
$poetryUrl = "https://install.python-poetry.org"

# Download the installation script
Invoke-WebRequest -Uri $poetryUrl -OutFile "install-poetry.py"

# Run the installation script with Python
python install-poetry.py

# Clean up by removing the installation script
Remove-Item -Path "install-poetry.py" -Force

# Add Poetry to the system PATH for the current session
$env:Path += ";$($env:USERPROFILE)\.local\bin"

# Verify the installation by printing the Poetry version
poetry --version

# Aguarda o usuário pressionar Enter antes de finalizar
Write-Host "Pressione Enter para finalizar..."
[System.Console]::ReadLine() | Out-Null