# Projeto Django2

```Python

# Error 1: instalando mysql, não funciona
# https://downloads.mysql.com/archives/community/
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" # para instalar o Homebrew
brew install mysql # instalar o MySQL
brew tap homebrew/services # iniciar o serviço MySQL
brew tap homebrew/services # Verificar se o serviço MySQL foi carregado
brew services start mysql # Verificar a instância MySQL instalada

brew update
brew upgrade
brew cleanup

brew install mysql@8.0

mysql --version
```