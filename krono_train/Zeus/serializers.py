from rest_framework import serializers
from .models import Cliente
from .models import Tienda
from .models import Subcategoria
from .models import Categoria
from .models import Producto
from .models import Canasta
from .models import Orden

class ClienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cliente
		fields = ('id','nombre', 'apellido', 'email')

class TiendaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tienda
		fields = ('id','nombre', 'ubicacion', 'clientes', 'categorias')

class SubcategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subcategoria
		fields = ('id','nombre', 'activa')

class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = ('id','nombre', 'activa', 'subcategorias')

class ProductoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Producto
		fields = ('id','nombre', 'precio', 'foto', 'subcategoria')

class CanastaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Canasta
		fields = ('id','productos', 'cliente', 'tienda')

class OrdenSerializer(serializers.ModelSerializer):
	class Meta:
		model = Orden
		fields = ('id','canasta')
