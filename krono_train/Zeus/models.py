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
		return dict(id=self.id,nombre=self.nombre, precio=self.precio, foto=self.foto, subcategoria=[ dict(id=subcategoria.id, nombre=subcategoria.nombre, activa=subcategoria.activa) for subcategoria in self.subcategoria.all()])

class Tienda(models.Model):
	nombre = models.CharField(max_length=100)
	ubicacion = models.CharField(max_length=1000)	
	clientes = models.ManyToManyField(Cliente)
	categorias = models.ManyToManyField(Categoria)		
	def as_json(self):
		return dict(id=self.id,nombre=self.nombre, ubicacion=self.ubicacion, clientes=[ dict(id=clientes.id, nombre=clientes.nombre, apellido=clientes.apellido, email=clientes.email) for clientes in self.clientes.all()], categorias=[ dict(id=categorias.id, nombre=categorias.nombre, activa=categorias.activa) for categorias in self.categorias.all()])

class Canasta(models.Model):
	productos = models.ManyToManyField(Producto)
	cliente = models.ForeignKey(Cliente)
	tienda = models.ForeignKey(Tienda)
	def as_json(self):
		return dict(id=self.id,productos=[ dict(id=productos.id, nombre=productos.nombre, precio=productos.precio, foto=productos.foto) for productos in self.productos.all()], cliente=dict(id=self.cliente.id, nombre= self.cliente.nombre, apellido=self.cliente.apellido, email=self.cliente.email), tienda=dict(id=self.tienda.id,nombre=self.tienda.nombre, ubicacion=self.tienda.ubicacion))

class Orden(models.Model):
	canasta = models.OneToOneField(Canasta)
	def as_json(self):
		return dict(id=self.id,id_canasta=self.canasta.id )