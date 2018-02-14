import json
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Cliente, Tienda, Subcategoria, Categoria, Producto, Canasta, Orden
from .serializers import ClienteSerializer, TiendaSerializer, SubcategoriaSerializer, CategoriaSerializer, ProductoSerializer, CanastaSerializer, OrdenSerializer

# Create your views here.

#Endpoint 1 | Todos los clientes
def get_users(request):
	queryset = Cliente.objects.all()
	return JsonResponse({ 'response':[ob.as_json() for ob in queryset], 'code': '0'}, safe=False)