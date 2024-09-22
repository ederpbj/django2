# Projeto Django2

```Python

# 1. Instalar pacotes 
pip install django whitenoise gunicorn django-bootstrap4 PyMySQL django-stdimage

pip freeze > requirements.txt

# 2. Criar projeto
django-admin startproject django2 .

# 3. Criar aplicação
django-admin startapp core

# 4. Instalando Postgres
brew install postgresql
brew services list # lista os serviços ativos
postgres --version

# Conectando projeto com pg
psql postgres # inicia o cliente
psql -U postgres -d django2db # conectar ao banco, como usuario postgres

# teste criar tabela, apagar depois
CREATE TABLE nome_da_tabela (
    id SERIAL PRIMARY KEY,
    coluna1 VARCHAR(255),
    coluna2 INTEGER
);

\dt # listar tabelas

# 5. Views


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