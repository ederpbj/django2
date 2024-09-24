from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from django.utils import timezone  # Importar timezone do Django
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Produto

from django.http import HttpResponse
from django.template import loader

from .forms import ContatoForm

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

# não grava os email no db
def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST': # significa que usuário fez envio
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada')
            print(f'Nome: {nome}')
            print(f'E-mail:  {email}')
            print(f'Assunto {assunto}')
            print(f'Mensagem: {mensagem}')

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)