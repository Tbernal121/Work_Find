from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .forms import ingresarAspiranteForm, ingresarEmpresaForm, ingresarOfertaForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

usr_id = 2
# Poner un if que pregunte si hay usuarios registrados
#usuarios_obj = Usuario.objects.get(id_usuario = usr_id)

def registro(request):
    if request.user.is_authenticated:
        return redirect('../')
    else:
        class CreateUserForm(UserCreationForm):
            class Meta:
                model = User
                fields = ['username', 'password1', 'password2']
        form = CreateUserForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                pwd = form.cleaned_data.get('password1')
                messages.success(request, 'La cuenta fue creada')
                messages.success(request, 'satisfactoriamente para ' + user)
                usuarioN = Usuario(nombre_usuario=user)
                usuarioN.save()
                user2 = authenticate(request, username=user, password=pwd)
                login(request, user2)
                return redirect('../')
                
        context = {'form': form}
        return render(request, 'registro.html', context)


def login1(request):
    if request.user.is_authenticated:
        return redirect('../')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('../')
            else:

                messages.info(request, 'Nombre de usuario o contrase??a')
                messages.info(request, 'est??n incorrectos')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('../login/')

@login_required(login_url='../login/')
def home(request):
    usuarios_obj = Usuario.objects.get(nombre_usuario=request.user)
    return render(request, 'home.html', {'nombre': usuarios_obj.nombre_usuario})

@login_required(login_url='../login/')
def homes(request):
    usuarios_obj = Usuario.objects.get(nombre_usuario=request.user)######################
    return render(request, 'homes.html', {'name':usuarios_obj.nombre_usuario})

@login_required(login_url='../login/')
def empresas(request): #cambios de mayusculas, homes es para pruebas
    info_tablaE = Empresa.objects.filter()
    usuarios_obj = Usuario.objects.get(nombre_usuario=request.user)
    return render(request, 'empresas.html', {'tabla_empresas': info_tablaE, 'name':usuarios_obj.nombre_usuario})

@login_required(login_url='../login/')
def aspirantes(request):
    info_tablaA = Aspirante.objects.filter()
    usuarios_obj = Usuario.objects.get(nombre_usuario=request.user)
    return render(request, 'aspirantes.html', {'tabla_aspirantes': info_tablaA, 'name':usuarios_obj.nombre_usuario})

@login_required(login_url='../login/')
def ofertas(request):
    info_tablaO = Oferta.objects.filter()
    usuarios_obj = Usuario.objects.get(nombre_usuario=request.user)
    return render(request, 'ofertas.html', {'tabla_ofertas': info_tablaO, 'name':usuarios_obj.nombre_usuario})


@login_required(login_url='../login/')
def documentacionAspirante(request):
    return render(request, 'docAspirante.html')

@login_required(login_url='../login/')
def documentacionEmpresa(request):
    return render(request, 'docEmpresa.html')

@login_required(login_url='../login/')
def ingresarOferta(request):
    #data={
    #   'formOferta': ingresarOfertaForm()
    #}
    #if request.method == 'POST':
    #    formulario = ingresarOfertaForm(data=request.POST)
    #    if formulario.is_valid():
    #        formulario.save()
    #        data["mensaje"] = "Oferta Guardada"
    #    else:
    #        data["formOferta"] =formulario
    #        data["mensaje"] = "Syntax Error"

    formulario = ingresarOfertaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, "Nueva oferta publicada con ??xito.")  # prueba de funcionalidad
        #return redirect('homes')
        return redirect('ofertas')

    return render(request, 'formularios/ingresarOferta.html', {'formulario': formulario})#data)


@login_required(login_url='../login/')
def ingresarEmpresa(request):
    #data={
    #   'formEmpresa': ingresarEmpresaForm()
    #}
    #if request.method == 'POST':
    #    formulario = ingresarEmpresaForm(data=request.POST)
    #    if formulario.is_valid():
    #        formulario.save()
    #        data["mensaje"] = "Oferta Guardada"
    #    else:
    #        data["formEmpresa"] =formulario
    #        data["mensaje"] = "Syntax Error"
    formulario = ingresarEmpresaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, "Nueva Empresa registrada con ??xito.")  # prueba de funcionalidad
        #return redirect('homes')
        return redirect('empresas')
    return render(request, 'formularios/ingresarEmpresa.html')

@login_required(login_url='../login/')
def ingresarAspirante(request):
    #data={
    #   'formAspirante': ingresarAspiranteForm()
    #}
    #if request.method == 'POST':
    #    formulario = ingresarAspiranteForm(data=request.POST)
    #    if formulario.is_valid():
    #        formulario.save()
    #        data["mensaje"] = "Oferta Guardada"
    #    else:
    #        data["formAspirante"] =formulario
    #        data["mensaje"] = "Syntax Error"
    formulario = ingresarAspiranteForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, "Nuevo Aspirante agregado con ??xito.")  # prueba de funcionalidad
        #return redirect('homes')
        return redirect('aspirantes')
    return render(request, 'formularios/ingresarAspirante.html')