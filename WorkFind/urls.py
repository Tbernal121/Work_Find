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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', vistas.home, name= 'home'),
    path('', vistas.homes, name = 'homes'),
    path('homes', vistas.homes, name = 'homes'),
    path('aspirantes', vistas.aspirantes, name= 'aspirantes'),
    path('empresas', vistas.empresas, name= 'empresas'),
    path('ofertas', vistas.ofertas, name= 'ofertas'),
    path('docEmpresa', vistas.documentacionEmpresa, name= 'docEmpresa'),
    path('docAspirante', vistas.documentacionAspirante, name= 'docAspirante'),

    path('ingresarOferta', vistas.ingresarOferta, name = 'ingresarOferta'),
    path('ingresarEmpresa', vistas.ingresarEmpresa, name = 'ingresarEmpresa'),
    path('ingresarAspirante', vistas.ingresarAspirante, name = 'ingresarAspirante'),

    path('login/', vistas.login1),
    path('registro/', vistas.registro),
    path('logout/', vistas.logoutUser),
]






'''
<div class="item separator borde">
                <a href="{% url 'matchs' %}">
                    <div class="icon"><abbr title="Matchs"><img style="padding-top:0.5em; padding-bottom:0.5em;" src="https://i.postimg.cc/Ssp1RDSr/enamorado.png" alt=""></abbr></div>
                    <div class="title" style="margin-top: 0.5em;"><span2><h6><font face="Poppins">Matchs</font></h6></span2></div>
                </a>
            </div>

'''


# from homes.html, line 316: 
'''
<th><a id="puntos1" href="{% url 'matchs' %}">
                    <img class="box" id="puntos2" width="150" alt="WhatsApp Logo"
                        src="https://i.postimg.cc/Ssp1RDSr/enamorado.png" /></a></th>

'''
