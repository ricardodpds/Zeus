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
		fields = ('nombre', 'apellido', 'email')

class TiendaSerializer(serializers.Serializer):
	class Meta:
		model = Tienda
		fields = ('nombre', 'ubicacion', 'clientes', 'categorias')

class SubcategoriaSerializer(serializers.Serializer):
	class Meta:
		model = Subcategoria
		fields = ('nombre', 'activa')

class CategoriaSerializer(serializers.Serializer):
	class Meta:
		model = Categoria
		fields = ('nombre', 'activa', 'subcategorias')

class ProductoSerializer(serializers.Serializer):
	class Meta:
		model = Producto
		fields = ('nombre', 'precio', 'foto', 'subcategoria')

class CanastaSerializer(serializers.Serializer):
	class Meta:
		model = Canasta
		fields = ('productos', 'cliente', 'tienda')

class OrdenSerializer(serializers.Serializer):
	class Meta:
		model = Orden
		fields = ('canasta')
