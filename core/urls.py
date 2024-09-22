from django.urls import path

# importa as views criadas em core
from .views import index, contato, produto

# Recebe as requisições de rotas do django
urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    #path('produto/<int:pk>', produto, name='produto')
    path('produto', produto, name='produto')
]