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

# gitignore
git rm -r --cached .
git add .
git commit -m "Remover arquivos do controle de versão e atualizar .gitignore"
git push origin mmaster

# 5. Views


```