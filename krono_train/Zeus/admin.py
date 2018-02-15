from django.contrib import admin

# Register your models here.
from .models import Cliente, Tienda, Subcategoria, Categoria, Producto, Canasta, Orden

admin.site.register(Cliente)
admin.site.register(Subcategoria)
admin.site.register(Categoria)
