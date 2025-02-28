from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Página de inicio
    path('acerca/', views.acerca, name='acerca'),
    path('administracion/', views.administracion, name='administracion'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('carrocompra/', views.carrocompra, name='carrocompra'),
    path('centrodeayuda/', views.centrodeayuda, name='centrodeayuda'),
    path('cerrar/', views.cerrar, name='cerrar'),
    path('convensocio/', views.convensocio, name='convensocio'),
    path('devoluciones/', views.devoluciones, name='devoluciones'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('ingresar/', views.ingresar, name='ingresar'),
    path('inversiones/', views.inversiones, name='inversiones'),
    path('lanzamientos/', views.lanzamientos, name='lanzamientos'),
    path('noticias/', views.noticias, name='noticias'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('perfil/', views.perfil, name='perfil'),
    path('registro/', views.registro, name='registro'),
    path('sustentabilidad/', views.sustentabilidad, name='sustentabilidad'),
    path('termnsycond/', views.termnsycond, name='termnsycond'),
    path('trabconnos/', views.trabconnos, name='trabconnos'),
    path('plantilla/', views.plantilla, name='plantilla'),
    path('inventario/', views.inventario, name='inventario'),
    path('ventas/', views.ventas, name='ventas'),
    path('compras/', views.compras, name='compras'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('informes/', views.informes, name='informes'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('pagar/', views.pagar, name='pagar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
