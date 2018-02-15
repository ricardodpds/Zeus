from rest_framework import serializers
from .models import Cliente
from .models import Tienda
from .models import Subcategoria
from .models import Categoria
from .models import Producto
from .models import Canasta
from .models import Orden

class ClienteSerializer(serializers.Serializer):
	class Meta:
		model = Cliente
		fields = ('id','nombre', 'apellido', 'email')

class TiendaSerializer(serializers.Serializer):
	class Meta:
		model = Tienda
		fields = ('id','nombre', 'ubicacion', 'clientes', 'categorias')

class SubcategoriaSerializer(serializers.Serializer):
	class Meta:
		model = Subcategoria
		fields = ('id','nombre', 'activa')

class CategoriaSerializer(serializers.Serializer):
	class Meta:
		model = Categoria
		fields = ('id','nombre', 'activa', 'subcategorias')

class ProductoSerializer(serializers.Serializer):
	class Meta:
		model = Producto
		fields = ('id','nombre', 'precio', 'foto', 'subcategoria')

class CanastaSerializer(serializers.Serializer):
	class Meta:
		model = Canasta
		fields = ('id','productos', 'cliente', 'tienda')

class OrdenSerializer(serializers.Serializer):
	class Meta:
		model = Orden
		fields = ('id','canasta')
