from django.shortcuts import render

from django.utils import timezone  # Importar timezone do Django
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Produto

from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def produto(request):
    return render(request, 'produto.html')

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)