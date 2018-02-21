import json
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Cliente, Tienda, Subcategoria, Categoria, Producto, Canasta, Orden
from .serializers import ClienteSerializer, TiendaSerializer, SubcategoriaSerializer, CategoriaSerializer, ProductoSerializer, CanastaSerializer, OrdenSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
# Create your views here.

#Endpoint 1 | Todos los clientes

#def get_users(request):
#	queryset = Cliente.objects.all()
#	return JsonResponse({ 'response':[ob.as_json() for ob in queryset], 'code': '0'}, safe=False)

def get_users(request):
	queryset = Cliente.objects.all()
	serializer = ClienteSerializer(queryset, many=True)
	return JsonResponse(serializer.data, safe=False)

def get_entity_user(request):
	return JsonResponse({ 'Cliente': {'id': 'integer','nombre': 'string','apellido': 'string', 'email': 'string', }} )

#Endpoints Clientes Crear | Editar | Delete
@api_view(['POST'])
def cliente_endpoint(request):
	try:		
		#Añadir
		if request.data['task'] == "add":
			serializer = ClienteSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse({'mensaje': 'Creado satisfactoriamente', 'code': '00'})
			return JsonResponse(serializer.errors, status=400)
		#Editar
		elif request.data['task'] == 'edit':			
			id_cliente = request.data['id']			
			queryset = Cliente.objects.filter(id=id_cliente)
			if queryset.count() > 0:
				serializer = ClienteSerializer(queryset[0], request.data)
				if serializer.is_valid():
					serializer.save()
					return JsonResponse({'mensaje': 'Editado satisfactoriamente', 'code': '00'})
				return JsonResponse(serializer.errors, status=400)
			else:
				return JsonResponse({'mensaje': 'No existe ese cliente en la base de datos', 'code' : '03'})
		#Eliminar
		elif request.data['task'] == 'delete':
			id_cliente = request.data['id']			
			queryset = Cliente.objects.filter(id=id_cliente)
			if queryset.count() > 0:
				queryset.delete()
				return JsonResponse({'mensaje': 'Eliminado satisfactoriamente', 'code': '00'})
			else:
				return JsonResponse({'mensaje': 'No existe ese cliente en la base de datos', 'code' : '03'})	
		#Error		
		else:
			return JsonResponse({'mensaje': 'Error - parametro task sin especificar', 'code' : '02'})
	except Exception as e:
		print(e)		
		return JsonResponse({'mensaje': 'Error - Datos enviados estan mal parametrizados', 'code' : '01'})

#Endpoint 2 | Todas las subcategorias
def get_subcategoria(request):	
	queryset = Subcategoria.objects.all()
	serializer = SubcategoriaSerializer(queryset, many=True)
	return JsonResponse(serializer.data, safe=False)

def get_entity_subcategoria(request):
	return JsonResponse({ 'Subcategoria': {'id': 'integer','nombre': 'string','activa': 'boolean' }} )

#Endpoints Clientes Crear | Editar | Delete
@api_view(['POST'])
def subcategoria_endpoint(request):
	try:		
		if request.data['task'] == "add":
			serializer = SubcategoriaSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse({'mensaje': 'Creado satisfactoriamente', 'code': '00'})
			return JsonResponse(serializer.errors, status=400)
		elif request.data['task'] == 'edit':
			id_subcategoria = request.data['id']			
			queryset = Subcategoria.objects.filter(id=id_subcategoria)
			if queryset.count() > 0:
				serializer = SubcategoriaSerializer(queryset[0], request.data)
				if serializer.is_valid():
					serializer.save()
					return JsonResponse({'mensaje': 'Editado satisfactoriamente', 'code': '00'})
				return JsonResponse(serializer.errors, status=400)
			else:
				return JsonResponse({'mensaje': 'No existe esa subcategoria en la base de datos', 'code' : '03'})
		elif request.data['task'] == 'delete':
			id_subcategoria = request.data['id']			
			queryset = Subcategoria.objects.filter(id=id_subcategoria)
			if queryset.count() > 0:
				queryset.delete()
				return JsonResponse({'mensaje': 'Eliminado satisfactoriamente', 'code': '00'})
			else:
				return JsonResponse({'mensaje': 'No existe esa subcategoria en la base de datos', 'code' : '03'})			
		else:
			return JsonResponse({'mensaje': 'Error - parámetro task sin especificar', 'code' : '02'})
	except Exception as e:
		print(e)		
		return JsonResponse({'mensaje': 'Error - Datos enviados están mal parametrizados', 'code' : '01'})

#Endpoint 3 | Todas las categoria 
def get_categoria(request):
	queryset = Categoria.objects.all()
	serializer = CategoriaSerializer(queryset, many=True)
	return JsonResponse(serializer.data, safe=False)

def get_entity_categoria(request):
	return JsonResponse({ 'Categoria': {'id': 'integer','nombre': 'string','activa': 'boolean', 'subcategorias': 'Array de Subcategorias' }} )

#Endpoints Categorias Crear | Editar | Delete
@api_view(['POST'])
def categoria_endpoint(request):
	try:		
		if request.data['task'] == "add":	
			serializer = CategoriaSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse({'mensaje': 'Creado satisfactoriamente', 'code': '00'})
			return JsonResponse(serializer.errors, status=400)
		elif request.data['task'] == 'edit':
			id_Categoria = request.data['id']
			queryset = Categoria.objects.filter(id=id_Categoria)
			if queryset.count() > 0:
				serializer = CategoriaSerializer(queryset[0], request.data)
				if serializer.is_valid():
					serializer.save()
					return JsonResponse({'mensaje': 'Editado satisfactoriamente', 'code': '00'})
				return JsonResponse(serializer.errors, status=400)
			else:
				return JsonResponse({'mensaje': 'No existe esa subcategoria en la base de datos', 'code' : '03'})			
		elif request.data['task'] == 'delete':
			id_Categoria = request.data['id']			
			queryset = Categoria.objects.filter(id=id_Categoria)
			if queryset.count() > 0:
				queryset.delete()
				return JsonResponse({'mensaje': 'Eliminado satisfactoriamente', 'code': '00'})
			else:
				return JsonResponse({'mensaje': 'No existe esa categoria en la base de datos', 'code' : '03'})			
		else:
			return JsonResponse({'mensaje': 'Error - parámetro task sin especificar', 'code' : '02'})
	except Exception as e:
		print(e)		
		return JsonResponse({'mensaje': 'Error - Datos enviados están mal parametrizados', 'code' : '01'})


#Endpoint 4 | Todos los productos 
def get_producto(request):
	queryset = Producto.objects.all()
	serializer = ProductoSerializer(queryset, many=True)
	return JsonResponse(serializer.data, safe=False)

def get_entity_producto(request):
	return JsonResponse({ 'Producto': {'id': 'integer','nombre': 'string','precio': 'double', 'foto': 'string','subcategorias': 'Array de Subcategorias' }} )

#Endpoints Categorias Crear | Editar | Delete
@api_view(['POST'])
def producto_endpoint(request):
	try:		
		if request.data['task'] == "add":	
			serializer = ProductoSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse({'mensaje': 'Creado satisfactoriamente', 'code': '00'})
			return JsonResponse(serializer.errors, status=400)
		elif request.data['task'] == 'edit':
			id_Producto = request.data['id']
			queryset = Producto.objects.filter(id=id_Producto)
			if queryset.count() > 0:
				serializer = ProductoSerializer(queryset[0], request.data)
				if serializer.is_valid():
					serializer.save()
					return JsonResponse({'mensaje': 'Editado satisfactoriamente', 'code': '00'})
				return JsonResponse(serializer.errors, status=400)
			else:
				return JsonResponse({'mensaje': 'No existe esa subcategoria en la base de datos', 'code' : '03'})			
		elif request.data['task'] == 'delete':
			id_Producto = request.data['id']			
			queryset = Producto.objects.filter(id=id_Producto)
			if queryset.count() > 0:
				queryset.delete()
				return JsonResponse({'mensaje': 'Eliminado satisfactoriamente', 'code': '00'})
			else:
				return JsonResponse({'mensaje': 'No existe esa producto en la base de datos', 'code' : '03'})			
		else:
			return JsonResponse({'mensaje': 'Error - parámetro task sin especificar', 'code' : '02'})
	except Exception as e:
		print(e)		
		return JsonResponse({'mensaje': 'Error - Datos enviados están mal parametrizados', 'code' : '01'})


def get_tienda(request):
	queryset = Tienda.objects.all()
	serializer = TiendaSerializer(queryset, many=True)
	return JsonResponse(serializer.data, safe=False)

def get_entity_tienda(request):
	return JsonResponse({ 'Tienda': {'id': 'integer','nombre': 'string', 'ubicacion': 'string','categorias': 'Array de Categorias', 'clientes': 'Array de Clientes' }} )

#Endpoints Tienda Crear | Editar | Delete
@api_view(['POST'])
def tienda_endpoint(request):
	try:		
		if request.data['task'] == "add":	
			serializer = TiendaSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse({'mensaje': 'Creado satisfactoriamente', 'code': '00'})
			return JsonResponse(serializer.errors, status=400)
		elif request.data['task'] == 'edit':
			id_Tienda = request.data['id']
			queryset = Tienda.objects.filter(id=id_Tienda)
			if queryset.count() > 0:
				serializer = TiendaSerializer(queryset[0], request.data)
				if serializer.is_valid():
					serializer.save()
					return JsonResponse({'mensaje': 'Editado satisfactoriamente', 'code': '00'})
				return JsonResponse(serializer.errors, status=400)
			else:
				return JsonResponse({'mensaje': 'No existe esa subcategoria en la base de datos', 'code' : '03'})			
		elif request.data['task'] == 'delete':
			id_Tienda = request.data['id']			
			queryset = Tienda.objects.filter(id=id_Tienda)
			if queryset.count() > 0:
				queryset.delete()
				return JsonResponse({'mensaje': 'Eliminado satisfactoriamente', 'code': '00'})
			else:
				return JsonResponse({'mensaje': 'No existe esa tienda en la base de datos', 'code' : '03'})			
		else:
			return JsonResponse({'mensaje': 'Error - parámetro task sin especificar', 'code' : '02'})
	except Exception as e:
		print(e)		
		return JsonResponse({'mensaje': 'Error - Datos enviados están mal parametrizados', 'code' : '01'})

#Endpoint 6 | Todas las canastas 
def get_canasta(request):
	queryset = Canasta.objects.all()
	serializer = CanastaSerializer(queryset, many=True)
	return JsonResponse(serializer.data, safe=False)

def get_entity_canasta(request):
	return JsonResponse({ 'Canasta': {'id': 'integer', 'productos': 'Array de Productos', 'cliente': 'Cliente', 'tienda': 'Tienda' }} )

#Endpoints Canasta Crear | Editar | Delete
@api_view(['POST'])
def canasta_endpoint(request):
	try:		
		if request.data['task'] == "add":	
			serializer = CanastaSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse({'mensaje': 'Creado satisfactoriamente', 'code': '00'})
			return JsonResponse(serializer.errors, status=400)			
		elif request.data['task'] == 'edit':
			id_Canasta = request.data['id']
			queryset = Canasta.objects.filter(id=id_Canasta)
			if queryset.count() > 0:
				serializer = CanastaSerializer(queryset[0], request.data)
				if serializer.is_valid():
					serializer.save()
					return JsonResponse({'mensaje': 'Editado satisfactoriamente', 'code': '00'})
				return JsonResponse(serializer.errors, status=400)
			else:
				return JsonResponse({'mensaje': 'No existe esa subcategoria en la base de datos', 'code' : '03'})
		elif request.data['task'] == 'delete':
			id_Canasta = request.data['id']			
			queryset = Canasta.objects.filter(id=id_Canasta)
			if queryset.count() > 0:
				queryset.delete()
				return JsonResponse({'mensaje': 'Eliminado satisfactoriamente', 'code': '00'})
			else:
				return JsonResponse({'mensaje': 'No existe esa Canasta en la base de datos', 'code' : '03'})			
		else:
			return JsonResponse({'mensaje': 'Error - parámetro task sin especificar', 'code' : '02'})
	except Exception as e:
		print(e)		
		return JsonResponse({'mensaje': 'Error - Datos enviados están mal parametrizados', 'code' : '01'})

#Endpoint 7 | Todas las ordenes 
def get_orden(request):
	queryset = Orden.objects.all()
	serializer = OrdenSerializer(queryset, many=True)
	return JsonResponse(serializer.data, safe=False)

def get_entity_orden(request):
	return JsonResponse({ 'Orden': {'id': 'integer', 'canasta': 'Canasta'}} )

#Endpoints Ordenes Crear | Editar | Delete
@api_view(['POST'])
def orden_endpoint(request):
	try:		
		if request.data['task'] == "add":				
			serializer = OrdenSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse({'mensaje': 'Creado satisfactoriamente', 'code': '00'})
			return JsonResponse(serializer.errors, status=400)			
		elif request.data['task'] == 'edit':			
			id_Orden = request.data['id']
			queryset = Orden.objects.filter(id=id_Orden)
			if queryset.count() > 0:
				serializer = OrdenSerializer(queryset[0], request.data)
				if serializer.is_valid():
					serializer.save()
					return JsonResponse({'mensaje': 'Editado satisfactoriamente', 'code': '00'})
				return JsonResponse(serializer.errors, status=400)
			else:
				return JsonResponse({'mensaje': 'No existe esa subcategoria en la base de datos', 'code' : '03'})			
		elif request.data['task'] == 'delete':
			id_Orden = request.data['id']			
			queryset = Orden.objects.filter(id=id_Orden)
			if queryset.count() > 0:
				queryset.delete()
				return JsonResponse({'mensaje': 'Eliminado satisfactoriamente', 'code': '00'})
			else:
				return JsonResponse({'mensaje': 'No existe esa Orden en la base de datos', 'code' : '03'})			
		else:
			return JsonResponse({'mensaje': 'Error - parámetro task sin especificar', 'code' : '02'})
	except Exception as e:
		print(e)		
		return JsonResponse({'mensaje': 'Error - Datos enviados están mal parametrizados', 'code' : '01'})