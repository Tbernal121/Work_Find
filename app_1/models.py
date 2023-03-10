from django.db import models
# Create your models here.


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
    Nombre_empresa = models.CharField(max_length=45, null=True, default="Coca-Cola")
    fecha_match = models.DateTimeField(auto_now_add=True)
    tipo_match = models.CharField(max_length=45, null=True,default="Perfecto", choices=(('Perfecto','Perfecto'),('Muy bueno', 'Muy bueno'),('Bueno','Bueno'),('Medio','Medio')))
    porcentaje = models.PositiveIntegerField(default=100)
