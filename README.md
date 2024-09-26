from gc import freezefrom distutils.command.install import installfrom ensurepip import bootstrap

# Projeto Django2

```Python
# 0. gitignore
git rm -r --cached .
git add .
git commit -m "Remover arquivos do controle de versão e atualizar .gitignore"
git push origin mmaster

# 1. Instalar pacotes 
pip install django whitenoise gunicorn django-bootstrap4 PyMySQL django-stdimage

pip freeze > requirements.txt

# 2. Criar projeto
django-admin startproject django2 .

# 3. Criar aplicação
django-admin startapp core

# 4 Postgres
# 4.1 Instalando Postgres
brew install postgresql
brew services list # lista os serviços ativos
postgres --version

# 4.2 Conectando projeto com pg
psql postgres # inicia o cliente
psql -U postgres -d django2db # conectar ao banco, como usuario postgres

# 4.3 teste criar tabela, apagar depois
CREATE TABLE nome_da_tabela (
    id SERIAL PRIMARY KEY,
    coluna1 VARCHAR(255),
    coluna2 INTEGER
);

\dt # listar tabelas

# 5. Criar Views
# core/views

# 6. Criar templates
# index, contato e produto

# 7. Criar pasta statics
# pastas static: css, images, js

# 8. Definindo rotas urls
# django2/urls
    # path("/", include('core.urls')),
# criar core/urls.py
    # referenciar todas as views

# 9. Migrando para db    
pip install psycopg2
pip install psycopg
    
pip freeze > requirements.txt

python manage.py migrate
python manage.py makemigrations # para atualizar o migrate

# 10. Criar super usuário
python manage.py createsuperuser
python manage.py runserver # rodar para testar

# 11. Coletar arquivos estaticos
python manage.py collectstatic

python manage.py check # verificacões

# 12. Criar form
# criar core/forms.py
# usar o shell, para ver as funções do form
python manage.py shell
from django import forms
dir(forms) # mostra as funções disponíveis
dir(forms.Form) # mostra as funções disponíveis
help(forms.Form.is_valid) # mostra as funções disponíveis

help(forms.CharField) # mostra atributos 

# atualizar core/views com o form

# 13. usando bootstrap no contato.html
# 14. Criar core/forms.py
# 15 executar migration
python manage.py makemigrations
python manage.py migrate


# 16. Registrar o core/admin

# criar super usuário
python manage.py createsuperuser

# pacote para imagens
#pip install django-pictures # nao funcionou
pip install django-imagekit
pip list # lista pacotes instalados

# 17. publicando no heroku
pip install dj_database_url psycopg2-binary

pip freeze > requirements.txt

# 18. criar arquivos ProcFile e runtime.txt, para heroko rodar
```
[docs bootstrap](https://getbootstrap.com/docs/5.3/content/tables/)
