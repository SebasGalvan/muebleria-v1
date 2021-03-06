from django.urls.conf import include
from CARRITO import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



# app_name = "CARRITO"
urlpatterns = [
    path('', views.inicio, name='Home'),
    path('buscar/', views.buscar, name='Buscar'),
    path('producto/', views.producto, name='Producto'),
    path('producto/<int:id>', views.productoEditar, name='EditarProducto'),
    path('eliminarProducto/<int:id>', views.productoEliminar, name='EliminarProducto'),
    path('producto/<int:id>/', views.verProducto, name='verProducto'), 
    path('agregarProducto/', views.agregarProducto, name='Agregar'), 
    path('contacto/', views.contacto, name='Contacto'),
    path('acerca_de/', views.acerca_de, name='Aacerca de'),
    path('carrito/', views.carrito, name='Carrito'),
    path('carrito/<int:id>', views.agregarCarrito, name='AgregarCarrito'),
    path('vaciarCarrito/', views.vaciarCarrito, name='vaciarCarrito'),
    path('eliminarCarrito/<int:id>', views.eliminarDelCarrito, name='EliminarDelCarrito'),
    path('USUARIO/', include('USUARIOS.urls')), 
    path('agregarCategoria/', views.agregarCategoria, name='AgregarCategoria'), 
    path('categoria/<int:id>', views.productoCategoria, name='Categoria'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)