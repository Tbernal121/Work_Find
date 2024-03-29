from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, blank=False)
    nombre_usuario = models.CharField(max_length=45, null=False)
    contrasena_usuario = models.CharField(max_length=45, null=False)
    tipo_usuario = models.CharField(max_length=45, null=False, choices=(('Empresa','Empresa'),('Aspirante', 'Aspirante')))

    def __str__(self):
        usuario = "nombre del Usuario: "+self.nombre_usuario
        return usuario

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True, blank=False) #de auto a integer para evitar duplicados
    Usuario_id_usuario = models.ForeignKey(Usuario, null= False, blank=False, on_delete=models.CASCADE)
    nombre_empresa = models.CharField(max_length=45, null=False)
    correo_empresa = models.CharField(max_length=45, null=False)
    presentacion_empresa = models.CharField(max_length=1000, null=False)
    nit = models.CharField(max_length=45, null=False)
    sectorEconomico = models.CharField(max_length=45, null=False)#, choices=(('Primario','Primario'),('Secundario', 'Secundario'),('Terciario','Terciario'),('Cuaternario','Cuaternario')))

    def __str__(self):
        empresa = "nombre de la Empresa: "+self.nombre_empresa
        return empresa


class Aspirante(models.Model):
    id_aspirante = models.AutoField(primary_key=True, blank=False)  #auto ainteger para evitar duplicados
    Usuario_id_usuario = models.ForeignKey(Usuario, null= False, blank=False, on_delete=models.CASCADE)
    nombre_aspirante = models.CharField(max_length=45, null=False)
    correo_aspirante = models.CharField(max_length=45, null=False)
    presentacion_aspirante = models.CharField(max_length=1000, null=False)
    cedulaciudadania = models.PositiveIntegerField(default=0)
    certificaciones = models.CharField(max_length=200, null=False)
    experiencia = models.CharField(max_length=1000, null=False)
    fecha_nacimiento = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    quien_me_likeo = models.CharField(max_length=1000)
    
    def __str__(self):
        aspirante = "nombre del Aspirante: "+self.nombre_aspirante
        return aspirante


class documentacionEmpresa(models.Model):
    Empresa_id_empresa = models.ForeignKey(Empresa, null= False, blank=False, on_delete=models.CASCADE)
    politicas = models.CharField(max_length=1000, null=False)
    tyc = models.CharField(max_length=1000, null=False)


class documentacionAspirante(models.Model):
    Aspirante_id_aspirante = models.ForeignKey(Aspirante, null= False, blank=False, on_delete=models.CASCADE)
    hdv = models.CharField(max_length=1000, null=False)
    recomendaciones = models.CharField(max_length=1000, null=False)


class Oferta(models.Model):
    id_Oferta = models.AutoField(primary_key=True, blank=False)
    Empresa_id_empresa = models.ForeignKey(Empresa, null= False, blank=False, on_delete=models.CASCADE)
    Nombre_empresa = models.CharField(max_length=45, null=True)
    cargo = models.CharField(max_length=45, null=False)
    perfil_buscado = models.CharField(max_length=200, null=False)
    salario = models.PositiveIntegerField(default=0)


class Match(models.Model):
    Oferta_id_oferta = models.ForeignKey(Oferta, null= False, blank=False, on_delete=models.CASCADE)
    Empresa_id_empresa = models.ForeignKey(Empresa, null= False, blank=False, on_delete=models.CASCADE)
    Aspirante_id_aspirante = models.ForeignKey(Aspirante, null= False, blank=False, on_delete=models.CASCADE)
    Nombre_empresa = models.CharField(max_length=45, null=True, default="") #default="MercadoLibre"
    fecha_match = models.DateTimeField(auto_now_add=True)
    tipo_match = models.CharField(max_length=45, null=True,default="Perfecto", choices=(('Perfecto','Perfecto'),('Muy bueno', 'Muy bueno'),('Bueno','Bueno'),('Medio','Medio')))
    porcentaje = models.PositiveIntegerField(default=100)
    #usuario_aspirante = info del aspirante para mostrarle a la empresa con quién específicamente ha hecho match y 
    #ya la empresa decide si contactarlos o no



        
# Esta clase se podría borrar y no le pasaría nada al modelo
class Ver_matchs(models.Model):
    Oferta_id_oferta = models.ForeignKey(Oferta, null= False, blank=False, on_delete=models.CASCADE)
    Empresa_id_empresa = models.ForeignKey(Empresa, null= False, blank=False, on_delete=models.CASCADE)
    Aspirante_id_aspirante = models.ForeignKey(Aspirante, null= False, blank=False, on_delete=models.CASCADE)
    Nombre_empresa = models.CharField(max_length=45, null=True, default="aaa") #default="MercadoLibre"
    fecha_match = models.DateTimeField(auto_now_add=True)
    tipo_match = models.CharField(max_length=45, null=True,default="Perfecto", choices=(('Perfecto','Perfecto'),('Muy bueno', 'Muy bueno'),('Bueno','Bueno'),('Medio','Medio')))
    porcentaje = models.PositiveIntegerField(default=100)
    #usuario_aspirante = info del aspirante para mostrarle a la empresa con quién específicamente ha hecho match y 
    #ya la empresa decide si contactarlos o no


class Habilidad1(models.Model):
    id_habilidad1 = models.AutoField(primary_key=True, blank=False)
    usuario = models.ForeignKey(Usuario, null= False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, null=True, default="")

    def _str_(self):
        return self.nombre



class ArchivoPDF(models.Model):
    archivo = models.FileField(upload_to='pdfs/')

'''
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    likes = models.IntegerField(default=0)'''