from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ValidationError
from django.contrib import messages

from ventas.models import *
from inventario.models import *

from datetime import datetime


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
        categoria = Categoria.objects.get(pkCategoria = idCategoria)
        newDescuento = DescuentoCategoria(
            fkCategoria = categoria,
            fechaInicio = fechaInicio,
            fechaFin = fechaFin,
            porcentajeDescuento = descuento
        )
        auxfechafin = datetime.strptime(fechaFin,'%Y-%m-%d')
        auxfechainicio = datetime.strptime(fechaFin,'%Y-%m-%d')
        difFechas = (auxfechafin-auxfechainicio).days
        fechaActual = (auxfechainicio-datetime.today()).days
        if(difFechas < 0 or fechaActual < -1):
            messages.info(request, 'La fecha de inicio no puede ser mayor que la fecha final')
            return render(request, "ventas/creardescuentos.html", context,{})
        try:
            newDescuento.full_clean()
        except:
            messages.info(request, 'Alguno(s) campo(s) no son validos')
            return render(request, "ventas/creardescuentos.html", context,{})
        newDescuento.save()
        messages.success(request, 'EL descuento ha sido creado exitosamente')
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
        auxfechafin = datetime.strptime(fechaFin,'%Y-%m-%d')
        auxfechainicio = datetime.strptime(fechaFin,'%Y-%m-%d')
        difFechas = (auxfechafin-auxfechainicio).days
        fechaActual = (auxfechainicio-datetime.today()).days
        if(difFechas < 0 or fechaActual < -1):
            messages.info(request, 'La fecha de inicio no puede ser mayor que la fecha final')
            return render(request, "ventas/creardescuentos.html", context,{})
        try:
            newDescuento.full_clean()
        except:
            messages.info(request, 'Alguno(s) campo(s) no son validos')
            return render(request, "ventas/creardescuentos.html", context,{})
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
        auxfechafin = datetime.strptime(fechaFin,'%Y-%m-%d')
        auxfechainicio = datetime.strptime(fechaFin,'%Y-%m-%d')
        difFechas = (auxfechafin-auxfechainicio).days
        fechaActual = (auxfechainicio-datetime.today()).days
        if(difFechas < 0 or fechaActual < -1):
            messages.info(request, 'La fecha de inicio no puede ser mayor que la fecha final')
            return render(request, "ventas/creardescuentos.html", context,{})
        try:
            newDescuento.full_clean()
        except:
            messages.info(request, 'Alguno(s) campo(s) no son validos')
            return render(request, "ventas/creardescuentos.html", context,{})
        newDescuento.save()
        messages.success(request, 'EL descuento ha sido creado exitosamente')
        return redirect(to='ventas:descuentoCrear')

    return render(request, "ventas/creardescuentos.html", context, {})



def descuentoCrud(request, *args, **kwargs):
    return render(request, "ventas/descuentosCRUD.html", {})


def descuentoConsultar(request, *args, **kwargs):
    accion = request.POST
    consultar = accion.get('consultarBoton')
    categoria = {}
    subcategoria = {}
    producto = {}
    
    if(consultar):
        try:
            tipo = accion.get('tipoConsulta')
            if (tipo == "categoria"):
                categoria = DescuentoCategoria.objects.all().order_by('fkCategoria__nombreCategoria', 'fechaInicio')
            elif (tipo == "subcategoria"):
                subcategoria = DescuentoSubCategoria.objects.all().order_by('fkSubCategoria__fkCategoria__nombreCategoria', 'fkSubCategoria__nombreSubCategoria', 'fechaInicio')
            elif (tipo == "producto"):
                producto = DescuentoProducto.objects.all().order_by('fkProducto__fkSubCategoria__fkCategoria__nombreCategoria', 'fkProducto__fkSubCategoria__nombreSubCategoria', 'fkProducto__nombre', 'fechaInicio')
            else:
                messages.info(request, 'Debe seleccionar un tipo de descuento para realizar una consulta')
        except:
            pass
    context={'categoria': categoria, 'subcategoria': subcategoria, 'producto': producto}
    return render(request, "ventas/descuentoConsultar.html", context, {})