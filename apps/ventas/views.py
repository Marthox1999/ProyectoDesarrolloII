from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ValidationError
from django.contrib import messages

from ventas.models import *
from inventario.models import *


# Create your views here.


def descuentos(request, *args, **kwargs):
    return render(request, "ventas/descuentos.html", {})

def crearDescuento(request):
    categorias = Categoria.objects.all()
    context={
        'categorias':categorias, 
        'subcategorias':[], 
        'productos':[],
        'categoria':0,
        'subcategoria':0,
        'producto':0
        }
    return render(request, "ventas/creardescuentos.html", context, {})

def crearDescuentoCategoria(request, idCategoria):
    categorias = Categoria.objects.all()
    subcategorias = SubCategoria.objects.filter(fkCategoria=idCategoria)
    categoria = idCategoria
    context={
        'categorias':categorias, 
        'subcategorias':subcategorias, 
        'productos':[],
        'categoria':categoria,
        'subcategoria':0,
        'producto':0
        }

    if request.method == 'POST':
        data = request.POST
        fechaInicio = data.get('fecha_inicio')
        fechaFin = data.get('fecha_fin')
        descuento = data.get('descuento')
        try:
            categoria = Categoria.objects.get(pkCategoria = idCategoria)
            newDescuento = DescuentoCategoria(
                fkCategoria = categoria,
                fechaInicio = fechaInicio,
                fechaFin = fechaFin,
                porcentajeDescuento = descuento
            )
            newDescuento.save()
            messages.success(request, 'EL descuento ha sido creado exitosamente')
        except:
            messages.info(request, 'Alguno(s) campo(s) no es(son) validos')
            return redirect(to='ventas:descuentoCrear')
        return redirect(to='ventas:descuentoCrear')

    return render(request, "ventas/creardescuentos.html", context, {})

def crearDescuentoSubCategoria(request, idCategoria, idSubCategoria):
    categorias = Categoria.objects.all()
    subcategorias = SubCategoria.objects.filter(fkCategoria=idCategoria)
    productos = Producto.objects.filter(fkSubCategoria=idSubCategoria)
    categoria = idCategoria
    subcategoria = idSubCategoria
    context={
        'categorias':categorias, 
        'subcategorias':subcategorias, 
        'productos':productos,
        'categoria':categoria,
        'subcategoria':subcategoria,
        'producto':0
        }
    if request.method == 'POST':
        data = request.POST
        fechaInicio = data.get('fecha_inicio')
        fechaFin = data.get('fecha_fin')
        descuento = data.get('descuento')
        subcategoria = SubCategoria.objects.get(pkSubCategoria = idSubCategoria)
        newDescuento = DescuentoSubCategoria(
            fkSubCategoria = subcategoria,
            fechaInicio = fechaInicio,
            fechaFin = fechaFin,
            porcentajeDescuento = descuento
        )
        newDescuento.save()
        messages.success(request, 'EL descuento ha sido creado exitosamente')
        return redirect(to='ventas:descuentoCrear')

    return render(request, "ventas/creardescuentos.html", context, {})


def crearDescuentoProducto(request, idCategoria, idSubCategoria, idProducto):
    categorias = Categoria.objects.all()
    subcategorias = SubCategoria.objects.filter(fkCategoria=idCategoria)
    productos = Producto.objects.filter(fkSubCategoria=idSubCategoria)
    categoria = idCategoria
    subcategoria = idSubCategoria
    producto = idProducto
    context={
        'categorias':categorias, 
        'subcategorias':subcategorias, 
        'productos':productos,
        'categoria':categoria,
        'subcategoria':subcategoria,
        'producto':producto
        }

    if request.method == 'POST':
        data = request.POST
        fechaInicio = data.get('fecha_inicio')
        fechaFin = data.get('fecha_fin')
        descuento = data.get('descuento')
        producto = Producto.objects.get(pkProducto = idProducto)
        newDescuento = DescuentoProducto(
            fkProducto = producto,
            fechaInicio = fechaInicio,
            fechaFin = fechaFin,
            porcentajeDescuento = descuento
        )
        newDescuento.save()
        messages.success(request, 'EL descuento ha sido creado exitosamente')
        return redirect(to='ventas:descuentoCrear')

    return render(request, "ventas/creardescuentos.html", context, {})