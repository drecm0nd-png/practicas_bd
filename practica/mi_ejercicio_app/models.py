from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=200)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f'Codigo: {self.codigo} Descripción: {self.descripcion}'
    
class Automovil (models.Model):
    matricula = models.CharField(max_length=6, unique=True)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    al_dia_impuestos = models.BooleanField(default=True)

    def __str__(self):
        return f'Matricula {self.matricula} Marca {self.marca}'
    
class Futbolista (models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Nombre: {self.nombre}'
    
class Instructor (models.Model):
    documento = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100, null=True)
    genero = models.CharField(max_length=100)
    ciudad_residencia = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, unique=True)
    correo = models.EmailField()
    profesion = models.CharField(max_length=150)
    especialidad = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    salario_basico = models.DecimalField(max_digits=10, decimal_places=2)
    programado = models.BooleanField(default=True)

    def __str__(self):
        return f'Num document: {self.documento} | Nombre: {self.nombre}'

class Futbolista(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Nombre {self.nombre}'

    def __str__(self):
        return f'Nombre alcalde: {self.nombre}'

class Municipio (models.Model):
    codigo_dane = models.CharField(max_length=10, unique=True)
    nombre_municipio = models.CharField(max_length=100)
    habitantes = models.PositiveIntegerField()
    municipio_vencino = models.TextField()

    def __str__(self):
        return f'Nombre municipio: {self.nombre_municipio}'
    
class Vereda (models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    # Enlazar la vereda con municipio Uno a Muchos.
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)

    def __str__(self):
        return f'Nombre vereda: {self.nombre}'
    
class Alcalde (models.Model):
    tipo_doc = models.CharField(max_length=5, default='C.C')
    documento = models.CharField(max_length=20, unique=True)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    correo = models.EmailField()
    municipio = models.ForeignKey('municipio', on_delete=models.CASCADE)
    municipio = models.OneToOneField(Municipio, on_delete=models.CASCADE)