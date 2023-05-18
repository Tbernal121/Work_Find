"""WorkFind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from app_1 import views as vistas
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', vistas.home, name= 'home'),
    path('', vistas.homes, name = 'homes'),
    path('homes', vistas.homes, name = 'homes'),
    path('aspirantes', vistas.aspirantes, name= 'aspirantes'),
    path('empresas', vistas.empresas, name= 'empresas'),
    path('ofertas', vistas.ofertas, name= 'ofertas'),
    path('matchs', vistas.matchs, name= 'matchs'),
    path('ver_matchs', vistas.ver_matchs, name = 'ver_matchs'),
    path('perfil', vistas.perfil, name= 'perfil'),

    path('docEmpresa', vistas.documentacionEmpresa, name= 'docEmpresa'),
    path('docAspirante', vistas.documentacionAspirante, name= 'docAspirante'),

    path('ingresarOferta', vistas.ingresarOferta, name = 'ingresarOferta'),
    path('ingresarEmpresa', vistas.ingresarEmpresa, name = 'ingresarEmpresa'),
    path('ingresarAspirante', vistas.ingresarAspirante, name = 'ingresarAspirante'),
    path('PresentarseOferta', vistas.aplicarOferta, name = 'PresentarseOferta'),


    path('login/', vistas.login1),
    path('registro/', vistas.registro),
    path('logout/', vistas.logoutUser),
    path('agregar_habilidad', vistas.agregar_habilidad, name='agregar_habilidad'),

    path('', vistas.simple_upload, name='agregar_habilidad')

    #path('ver_matchs', vistas.ver_matchs, name = 'ver_matchs'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





'''
<div class="item separator borde">
                <a href="{% url 'matchs' %}">
                    <div class="icon"><abbr title="Matchs"><img style="padding-top:0.5em; padding-bottom:0.5em;" src="https://i.postimg.cc/Ssp1RDSr/enamorado.png" alt=""></abbr></div>
                    <div class="title" style="margin-top: 0.5em;"><span2><h6><font face="Poppins">Matchs</font></h6></span2></div>
                </a>
            </div>

'''