"""krono_train URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path
from django.conf.urls import url, include
from Zeus import views


urlpatterns = [
    #Endpoint | Admin
    url(r'^admin/', admin.site.urls),
    #Endpoint | Mostrar clientes
    url(r'^Zeus/clientes', views.get_users),
    #Endpoint | Cliente    
    url(r'^Zeus/clientes_endpoint', views.cliente_endpoint),
    #Endpoint | entity
    url(r'^Zeus/cliente_entity', views.get_entity_user),

     #Endpoint | Mostrar Subcategorias
    url(r'^Zeus/subcategorias/', views.get_subcategoria),
    #Endpoint | Subcategorias    
    url(r'^Zeus/subcategorias_endpoint', views.subcategoria_endpoint),
    #Endpoint | entity
    url(r'^Zeus/subcategoria_entity', views.get_entity_subcategoria),

    #Endpoint | Mostrar categorias
    url(r'^Zeus/categorias/', views.get_categoria),
    #Endpoint | Categoria    
    url(r'^Zeus/categorias_endpoint', views.categoria_endpoint),
    #Endpoint | entity
    url(r'^Zeus/categoria_entity', views.get_entity_categoria),

    #Endpoint | Mostrar Producto
    url(r'^Zeus/productos/', views.get_producto),
    #Endpoint | Producto    
    url(r'^Zeus/productos_endpoint', views.producto_endpoint),
    #Endpoint | entity
    url(r'^Zeus/producto_entity', views.get_entity_producto),

    #Endpoint | Mostrar Tienda
    url(r'^Zeus/tiendas/', views.get_tienda),
    #Endpoint | Tienda    
    url(r'^Zeus/tiendas_endpoint', views.tienda_endpoint),
    #Endpoint | entity
    url(r'^Zeus/tienda_entity', views.get_entity_tienda),

    #Endpoint | Mostrar Canasta
    url(r'^Zeus/canastas/', views.get_canasta),
    #Endpoint | Canasta    
    url(r'^Zeus/canastas_endpoint', views.canasta_endpoint),
    #Endpoint | entity
    url(r'^Zeus/canasta_entity', views.get_entity_canasta),

    #Endpoint | Mostrar Canasta
    url(r'^Zeus/ordenes/', views.get_orden),
    #Endpoint | Canasta    
    url(r'^Zeus/ordenes_endpoint', views.orden_endpoint),
    #Endpoint | entity
    url(r'^Zeus/orden_entity', views.get_entity_orden),
]