from django.db import models

# Create your models here.

class Cliente(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	def as_json(self):
		return dict(id=self.id, nombre=self.nombre, apellido=self.apellido, email=self.email)

class Subcategoria(models.Model):
	nombre = models.CharField(max_length=100)
	activa = models.BooleanField()	
	def as_json(self):
		return dict(id=self.id,nombre=self.nombre, activa=self.activa)

class Categoria(models.Model):
	nombre = models.CharField(max_length=100)
	activa = models.BooleanField()
	subcategorias = models.ManyToManyField(Subcategoria)
	def as_json(self):
		return dict(id=self.id,nombre=self.nombre, activa=self.activa, subcategorias=[ dict(id=subcategorias.id, nombre=subcategorias.nombre, activa=subcategorias.activa) for subcategorias in self.subcategorias.all()])

class Producto(models.Model):
	nombre = models.CharField(max_length=100)
	precio = models.FloatField(null=True)
	foto = models.CharField(max_length=500)
	subcategoria = models.ManyToManyField(Subcategoria)
	def as_json(self):
		return dict(id=self.id,nombre=self.nombre, precio=self.precio, foto=self.foto, subcategoria=self.subcategoria)

class Tienda(models.Model):
	nombre = models.CharField(max_length=100)
	ubicacion = models.CharField(max_length=1000)	
	clientes = models.ManyToManyField(Cliente)
	categorias = models.ManyToManyField(Categoria)		
	def as_json(self):
		return dict(id=self.id,nombre=self.nombre, ubicacion=self.ubicacion, clientes=self.clientes, categorias=self.categorias)

class Canasta(models.Model):
	productos = models.ManyToManyField(Producto)
	cliente = models.OneToOneField(Cliente)
	tienda = models.OneToOneField(Tienda)
	def as_json(self):
		return dict(id=self.id,productos=self.productos, cliente=self.cliente, tienda=self.tienda)

class Orden(models.Model):
	canasta = models.OneToOneField(Canasta)
	def as_json(self):
		return dict(id=self.id,canasta=self.canasta)