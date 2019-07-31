
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from usuarios.models import AdministradorDuenio
from django.core.exceptions import ValidationError
from django.utils import timezone
from usuarios.models import Cliente
from inventario.models import Categoria


def clienteIngreso(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    ingresar = request.POST
    context={'categorias':categorias, 'nombre':'noRegistrado'}
    if(request.method == 'POST'):
        aux = Cliente(
            nombre=ingresar.get('username'),
            clave=ingresar.get('password'),
            fechaNacimiento = timezone.now,
            direccion = "",
            telefono = "",
            tipoDocumento = "",
            numeroDocumento = 1234567,
        )
        nombre=ingresar.get('username')
        if (aux.autenticarCliente()):
            context={'categorias':categorias, 'nombre':nombre}
            messages.success(request, f'¡Bienvenido {nombre}!')
            return render(request, 'usuarios/clienteinicio.html', context,{})
        else:
            messages.info(request, 'Cuenta de usuario o contraseña invalida')
    return render(request, 'usuarios/clienteingreso.html', context,{'form':ingresar})

def clienteCerrarSesion(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    return render(request, 'usuarios/clienteingreso.html', context, {})

def clienteInicio(request, nombre):
    categorias = Categoria.objects.all()
    context={'categorias':categorias, 'nombre': nombre}
    return render(request, 'usuarios/clienteinicio.html', context, {})

@csrf_protect
def clienteregistro(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias, 'nombre':'noRegistrado'}
    registrar = request.POST
    if(request.method == 'POST'):
        aux = Cliente(
            nombre= registrar.get('nombreCliente'),
            clave = registrar.get('claveCliente'),
            fechaNacimiento = registrar.get('fechaNacimiento'),
            direccion = registrar.get('direccionCliente'),
            telefono = registrar.get('telefonoCliente'),
            tipoDocumento = registrar.get('tipoDocumento'),
            numeroDocumento = registrar.get('documentoCliente'),
        )
        try:
            aux.full_clean()
        except ValidationError as e:
            messages.info(request, 'Alguno(s) campo(s) no son validos')
            context={'categorias':categorias, 'nombre': 'noRegistrado'}
            return render(request, "usuarios/clienteregistro.html", context,{'form':registrar})
        nombre =registrar.get('nombreCliente')
        aux.save()
        messages.success(request, f'¡{nombre} bienvenido(a) a Nova!')
        return render(request, 'usuarios/clienteingreso.html', context,{})

    return render(request, "usuarios/clienteregistro.html",context, {'form':registrar})

def paginaPrincipal_admin(request):
    categorias = Categoria.objects.all()
    admin = AdministradorDuenio.objects.get(pkAdministradorDuenio =  1)
    #admin = get_object_or_404(AdministradorDuenio, pkAdministradorDuenio=id_dueno)
    context = {
        'objeto' : admin,
        'categorias': categorias
    }
    return render(request, "usuarios/paginaPrincipal_admin.html",context)

def paginaPrincipal_duenio(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    duenio = AdministradorDuenio.objects.get(pkAdministradorDuenio=1)
    context = {
        'objeto' : duenio,
        'categorias': categorias
    }
    return render(request, "usuarios/paginaPrincipal_duenio.html",context)


def duenioAdminAgregar(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    agregar = request.POST
    if(request.method=='POST'):
        admin=AdministradorDuenio(
            nombreUsuario=agregar.get('nombreAdmin'),
            clave=agregar.get('claveAdmin'),
            tipo='ADMIN'
        )
        try:
            admin.full_clean()
        except ValidationError as e:
            messages.info(request, 'Alguno(s) campo(s) no son validos')
            return render(request, "usuarios/duenioAdminAgregar.html",context,{'form':agregar})
        nombre =agregar.get('nombreAdmin')
        admin.save()
        messages.success(request, f'¡Bienvenido {nombre} !')
        return redirect(to='usuarios:duenioAgregarAdmin')
    return render(request,"usuarios/duenioAdminAgregar.html",context,{'form':agregar})


def adminMenu(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    return render(request,"usuarios/adminMenu.html",context, {})


def duenioAdminIngreso(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    ingresar = request.POST
    if(request.method == 'POST'):
        admin = AdministradorDuenio(
            nombreUsuario=ingresar.get('nombreDuenioAdmin'),
            clave=ingresar.get('claveDuenioAdmin'),
            tipo='ADMIN'
        )

        duenio=AdministradorDuenio(
            nombreUsuario=ingresar.get('nombreDuenioAdmin'),
            clave=ingresar.get('claveDuenioAdmin'),
            tipo='CEO'
        )
        nombre=ingresar.get('nombreDuenioAdmin')
        if (admin.autenticarAdmin()):
            messages.success(request, f'¡Bienvenido {nombre}!')
            return redirect(to='usuarios:paginaPrincipal_admin')
        elif (duenio.autenticarDuenio()):
            print("entra al elif")
            messages.success(request, f'¡Bienvenido {nombre}!')
            return redirect(to='usuarios:paginaPrincipal_duenio')
        else:
            messages.info(request, 'Cuenta de usuario o contraseña invalida')
    return render(request, 'usuarios/duenioAdminIngreso.html',context,{'form':ingresar})


def clientePerfil(request, nombre):
    context = {'nombre':nombre}
    return render(request,"usuarios/clientePerfil.html", context, {})
