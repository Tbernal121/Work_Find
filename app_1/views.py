from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib import messages
from .forms import ingresarAspiranteForm, ingresarEmpresaForm, ingresarOfertaForm, PresentarseOfertaForm, HabilidadForm, ArchivoPDFForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.

usr_id = 2
usuarios_obj = Usuario.objects.get(id_usuario = usr_id)

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

                messages.info(request, 'Nombre de usuario o contraseña')
                messages.info(request, 'están incorrectos')

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
    usuarios_obj = Usuario.objects.get(nombre_usuario=request.user)
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
    if request.method == 'POST':
        usuario_que_likeo = request.POST.get('usuario')
        context = {
            'tabla_aspirantes': info_tablaA,
            'name': usuarios_obj.nombre_usuario,
            'usuario_que_likeo': usuario_que_likeo,
        }
        return render(request, 'aspirantes.html', context)
    else:
        context = {
            'tabla_aspirantes': info_tablaA,
            'name': usuarios_obj.nombre_usuario,
        }
        return render(request, 'aspirantes.html', context)


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
        messages.success(request, "Nueva oferta publicada con éxito.")  # prueba de funcionalidad
        #return redirect('homes')
        return redirect('ofertas')

    return render(request, 'formularios/ingresarOferta.html', {'formulario': formulario})#data)


@login_required(login_url='../login/')
def aplicarOferta(request):
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

    formulario = PresentarseOfertaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, "Has aplicado exitosamente")  # prueba de funcionalidad
        #return redirect('homes')
        return redirect('ofertas')

    return render(request, 'formularios/PresentarseOferta.html', {'formulario': formulario})#data)



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
        messages.success(request, "Nueva Empresa registrada con éxito.")  # prueba de funcionalidad
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
        messages.success(request, "Nuevo Aspirante agregado con éxito.")  # prueba de funcionalidad
        #return redirect('homes')
        return redirect('aspirantes')
    return render(request, 'formularios/ingresarAspirante.html')


@login_required(login_url='../login/')
def matchs(request):
    info_tablaM = Match.objects.filter()
    usuarios_obj = Usuario.objects.get(nombre_usuario=request.user)
    return render(request, 'matchs.html', {'tabla_matchs': info_tablaM, 'name':usuarios_obj.nombre_usuario})


@login_required(login_url='../login/')
def ver_matchs(request):
    info_tablaVM = Match.objects.filter()
    usuarios_obj = Usuario.objects.get(nombre_usuario=request.user)
    return render(request, 'ver_matchs.html', {'tabla_ver_matchs': info_tablaVM, 'name':usuarios_obj.nombre_usuario})


@login_required
def agregar_habilidad(request):
    formulario = HabilidadForm(request.POST or None)
    if formulario.is_valid():
        habilidad = formulario.save(commit=False)
        usuario = Usuario.objects.get(nombre_usuario=request.user.username)
        habilidad.usuario = usuario
        habilidad.save()
        messages.success(request, "Nueva habilidad registrada con éxito.")
        return redirect('perfil')
    return render(request, 'formularios/ingresarHabilidad.html', {'formulario': formulario})




def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'formularios/ingresarHabilidad.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'formularios/ingresarHabilidad.html')

@login_required(login_url='../login/')
def perfil(request):
    usuarios_obj = Usuario.objects.get(nombre_usuario=request.user)
    return render(request, 'perfil.html', {'name':usuarios_obj.nombre_usuario})






def cargar_pdf(request):
    if request.method == 'POST':
        form = ArchivoPDFForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio después de guardar el archivo
    else:
        form = ArchivoPDFForm()
    return render(request, 'cargar_pdf.html', {'form': form})
