from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Classe base
class Base(models.Model):
    criado = models.DateTimeField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

# Produto
class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Estoque')
    imagem = models.ImageField(upload_to='products/', default='default.jpg')
    is_active = models.BooleanField(default=True)
    # Cria uma versão da imagem redimensionada para thumbnail
    thumbnail = ImageSpecField(source='imagem',
                                processors=[ResizeToFill(100, 100)],
                                format='JPEG',
                                options={'quality': 60})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

# Função pre_save para gerar o slug
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

# Conectando o sinal pre_save ao modelo Produto
signals.pre_save.connect(produto_pre_save, sender=Produto)



"""
class Contato(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        # return self.nome
        return f'{self.nome} {self.sobrenome}'
"""