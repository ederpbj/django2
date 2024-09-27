"""
URL configuration for django2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500

from core import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('painel/', admin.site.urls), # recomenda-se mudar de admin para outro ex painel
    # Cada aplicação define suas rotas
    path('', include('core.urls')), # Rotas gerenciadas pela aplicação core
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Acesso aos arquivos de midia

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.error404
handler500 = views.error500