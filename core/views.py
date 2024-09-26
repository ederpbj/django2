from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages

from .models import Produto


# Create your views here.
def index(request):
    context ={
        'produtos': Produto.objects.all() # lista os produtos no index
    }
    return render(request, 'index.html', context)

# não grava os email no db
def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST': # significa que usuário fez envio
        if form.is_valid():
            form.send_mail()
            """ Não precisa mais
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada')
            print(f'Nome: {nome}')
            print(f'E-mail:  {email}')
            print(f'Assunto {assunto}')
            print(f'Mensagem: {mensagem}')
            """
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            """
            prod = form.save(commit=False) # ainda nao salva no db
            print(f'Nome: {prod.nome}')
            print(f'Preco: {prod.preco}')
            print(f'Estoque: {prod.estoque}')
            print(f'Imagem: {prod.imagem}')
            """
            form.save() # salva no banco de dados

            messages.success(request, 'Produto salvo com sucesso!')
            form = ProdutoModelForm()
        else: # form invalido
            messages.error(request, 'Erro ao salva o produto!')
    else: # caso nao seja do tipo post
        form = ProdutoModelForm() # limpa o formulario
    context = {
        'form': form
    }

    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)