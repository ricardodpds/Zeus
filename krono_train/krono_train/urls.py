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
    url(r'^Zeus/clientes/', views.get_users),
    #Endpoint | Cliente    
    url(r'^Zeus/clientes_endpoint', views.cliente_endpoint),

     #Endpoint | Mostrar Subcategorias
    url(r'^Zeus/subcategorias/', views.get_subcategoria),
    #Endpoint | Subcategorias    
    url(r'^Zeus/subcategorias_endpoint', views.subcategoria_endpoint),

    #Endpoint | Mostrar categorias
    url(r'^Zeus/categorias/', views.get_categoria),
    #Endpoint | Categoria    
    url(r'^Zeus/categorias_endpoint', views.categoria_endpoint),

    #Endpoint | Mostrar Producto
    url(r'^Zeus/productos/', views.get_producto),
    #Endpoint | Producto    
    url(r'^Zeus/productos_endpoint', views.producto_endpoint),

    #Endpoint | Mostrar Tienda
    url(r'^Zeus/tiendas/', views.get_tienda),
    #Endpoint | Tienda    
    url(r'^Zeus/tiendas_endpoint', views.tienda_endpoint),
    
   # url(r'^api_test/shops/(?P<userid>\d+)/$', views.get_tiendas_by_id),
    #Endpoint3
   # url(r'^api_test/shops_city/user=(?P<user>\d+)&city=(?P<city>\d+)/$', views.get_tiendas_by_city),
    #Errores
   # url(r'^api_test/shops_city/', views.get_error_shops_city),
   # url(r'^api_test/users/', views.get_error_id),
    #url(r'^api_test/shops/', views.get_error_id),
]