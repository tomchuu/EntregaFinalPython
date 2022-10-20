
from re import template
from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("gimnasio", gimnasio, name="Gimnasio"),
    path("cliente", cliente, name="Cliente"),
    path("rutinas", rutinas, name="Rutinas"),
    path("form1/", formulario1, name="AgregarRutinas"),
    path("form2/", formulario2, name="AgregarCliente"),
    path("form3/", formulario3),
    path("buscarRutinas/", busquedaRutinas),
    path("buscar/", buscar),
    path("leerClientes", leerClientes, name="Cliente"),
    path("leerRutinas", leerRutinas, name="Rutinas"),
    path("borrarClientes/<clienteNombre>", borrarClientes, name="EliminarClientes"),
    path("borrarRutinas/<rutinaNombre>", borrarRutinas, name="EliminarRutinas"),
    path("editarRutinas/<rutinaNombre>", editarRutina, name="EditarRutinas"),
    path("login/", inicioSesion, name="Login"),
    path("register/", registro, name="SignUp"),
    path("logout", LogoutView.as_view(template_name="AppCoder/logout.html"), name="Logout"),
    path("editar", editarUsuario, name="EditarUsuario"),
    path("agregar/", agregarAvatar, name="Avatar"),
    path("about", about, name="SobreMi"),
]