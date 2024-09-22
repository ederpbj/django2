from django.db import models

# Create your models here.
# Lembrar de configurar django1/settings/INSTALLED_APPS/core
class Produto(models.Model):
    nome = models.CharField('Nome', max_length=1000)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.nome
        # return f'{self.nome} | Em Estoque: {self.estoque}'

class Contato(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        # return self.nome
        return f'{self.nome} {self.sobrenome}'