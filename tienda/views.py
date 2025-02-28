import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Producto
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Carrito
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def index(request):
    productos = Producto.objects.all()
    carrito = Carrito.objects.filter(usuario=request.user)
    context = {
        'productos': productos,
        'carrito': carrito,
    }
    return render(request, 'index.html', context)

def acerca(request):
    context = {}
    return render(request, 'tienda/acerca.html', context)

def administracion(request):
    context = {}
    return render(request, 'tienda/administracion.html', context)

def ayuda(request):
    context = {}
    return render(request, 'tienda/ayuda.html', context)

def carrocompra(request):
    context = {}
    return render(request, 'tienda/carrocompra.html', context)

def centrodeayuda(request):
    context = {}
    return render(request, 'tienda/centrodeayuda.html', context)

def cerrar(request):
    context = {}
    return render(request, 'tienda/cerrar.html', context)

def convensocio(request):
    context = {}
    return render(request, 'tienda/convensocio.html', context)

def devoluciones(request):
    context = {}
    return render(request, 'tienda/devoluciones.html', context)

def favoritos(request):
    context = {}
    return render(request, 'tienda/favoritos.html', context)

def ingresar(request):
    context = {}
    return render(request, 'tienda/ingresar.html', context)

def inversiones(request):
    context = {}
    return render(request, 'tienda/inversiones.html', context)

def lanzamientos(request):
    context = {}
    return render(request, 'tienda/lanzamientos.html', context)

def noticias(request):
    context = {}
    return render(request, 'tienda/noticias.html', context)

def ofertas(request):
    context = {}
    return render(request, 'tienda/ofertas.html', context)

@login_required
def perfil(request):
    context = {
        'user': request.user  # Pasa el usuario autenticado al contexto
    }
    return render(request, 'tienda/perfil.html', context)

def registro(request):
    context = {}
    return render(request, 'tienda/registro.html', context)

def sustentabilidad(request):
    context = {}
    return render(request, 'tienda/sustentabilidad.html', context)

def termnsycond(request):
    context = {}
    return render(request, 'tienda/termnsycond.html', context)

def trabconnos(request):
    context = {}
    return render(request, 'tienda/trabconnos.html', context)

def index(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/index.html', {'productos': productos})

def plantilla(request):
    context = {}
    return render(request, 'tienda/plantilla.html', context)

def probado(request):
    context = {}
    return render(request, 'tienda/probado.html', context)

def inventario(request):
    context = {}
    return render(request, 'tienda/inventario.html', context)

def ventas(request):
    context = {}
    return render(request, 'tienda/ventas.html', context)

def compras(request):
    context = {}
    return render(request, 'tienda/compras.html', context)

def usuarios(request):
    context = {}
    return render(request, 'tienda/usuarios.html', context)

def informes(request):
    context = {}
    return render(request, 'tienda/informes.html', context)

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if producto.stock > 0:
        carrito_item, created = Carrito.objects.get_or_create(usuario=request.user, producto=producto)
        carrito_item.cantidad += 1
        producto.stock -= 1
        carrito_item.save()
        producto.save()
        messages.success(request, 'Producto agregado al carrito.')
    else:
        messages.error(request, 'No hay suficiente stock para este producto.')
    return redirect('index')  # Redirigir a la página principal

@csrf_exempt
def pagar(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        productos = data.get('productos', {})

        for producto_id, producto_data in productos.items():
            producto = Producto.objects.get(id=producto_id)
            producto.stock -= producto_data['cantidad']
            producto.save()

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'fail'}, status=400)