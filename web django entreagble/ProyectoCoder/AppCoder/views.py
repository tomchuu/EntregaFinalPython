from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.



def inicioSesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contra)

            if user:

                login (request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {user}"})


        else:

            return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})

    else :

        form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"formulario":form})


def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":"Usuario creado."})


    else:

        form = UsuarioRegistro()

    return render(request, "AppCoder/registro.html", {"formulario":form})

@login_required
def editarUsuario(request):

    usuario = request.user

    if request.method == "POST":

        form = FormularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        form = FormularioEditar(initial={"email":usuario.email, "first_name":usuario.first_name, "last_name":usuario.last_name})
      

    return render(request, "AppCoder/editarPerfil.html", {"formulario":form, "usuario":usuario})







def inicio(request):
    
    return render(request, "AppCoder/inicio.html")


def about(request):
    return render(request, 'AppCoder/about.html')


def gimnasio(request):
    
    return render(request, "AppCoder/gimnasio.html")




def cliente (request):
    
    return render(request, "AppCoder/cliente.html")



def rutinas(request):
    
    return render(request, "AppCoder/rutinas.html")


def formulario1(request):

    if request.method =="POST":

        formulario1 = FormularioRutinas(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            rutinaF = Rutinas(nombre=info["nombre"], dias=info["dias"])

            rutinaF.save()

            return render(request, "AppCoder/inicio.html")


    else:

        formulario1=FormularioRutinas()

    
    return render(request, "AppCoder/formu1.html", {"form1":formulario1})



def formulario2(request):

    if request.method=="POST":

        formulario2 = FormularioCliente(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            clienteF = Cliente(nombre=info["nombre"], apellido=info["apellido"], fechadeingreso=info["fechadeingreso"])

            clienteF.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario2 = FormularioCliente()


    return render(request, "AppCoder/formu2.html", {"form2":formulario2})



def formulario3(request):

    if request.method=="POST":

        formulario3 = FormularioGimnasio(request.POST)

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            gimnasioF = Gimnasio(nombre=info["nombre"], valoracion=info["valoracion"])

            gimnasioF.save()

            return render(request, "AppCoder/gimnasio.html")

    else:

        formulario3 = FormularioGimnasio()

    return render(request, "AppCoder/formu3.html", {"form3":formulario3})



def busquedaRutinas(request):

    return render(request, "AppCoder/inicio.html")


def buscar(request):


    if request.GET["rutinas"]:
     
     busqueda = request.GET["rutinas"]
     rutinas = Rutinas.objects.filter(nombre__icontains=busqueda)
     
     return render(request, "AppCoder/inicio.html", {"rutinas":rutinas, "busqueda":busqueda} )

    else :
        
        mensaje = "No ingresaste datos."

  
    return HttpResponse(mensaje)


@login_required
def leerClientes(request):

    clients = Cliente.objects.all()

    contexto = {"clients":clients}

    return render(request, "AppCoder/cliente.html", contexto)


@login_required
def leerRutinas(request):

    rutins = Rutinas.objects.all()

    contexto = {"rutins":rutins}

    return render(request, "AppCoder/rutinas.html", contexto)



@login_required
def borrarClientes(request, clienteNombre):

    cliente = Cliente.objects.get(nombre=clienteNombre)

    cliente.delete()

    clients = Cliente.objects.all()

    contexto = {"clients":clients}

    return render(request, "AppCoder/cliente.html", contexto)


@login_required
def borrarRutinas(request, rutinaNombre):

    rutina = Rutinas.objects.get(nombre=rutinaNombre)

    rutina.delete()

    rutins = Rutinas.objects.all()

    contexto = {"rutins":rutins}

    return render(request, "AppCoder/rutinas.html", contexto)


@login_required
def editarRutina(request, rutinaNombre):

    rutina = Rutinas.objects.get(nombre=rutinaNombre)

    if request.method =="POST":
         
        formulario1 = FormularioRutinas(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            rutina.nombre = info["nombre"]
            rutina.dias = info["dias"]

            rutina.save()
            

            return render(request, "AppCoder/inicio.html")


    else:

        formulario1=FormularioRutinas(initial={"nombre":rutina.nombre, "dias":rutina.dias})

    contexto = {"form1":formulario1, "rutinaNombre":rutinaNombre}
    return render(request, "AppCoder/editarRutinas.html", contexto)




@login_required
def agregarAvatar(request):

    if request.method=="POST":

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "AppCoder/inicio.html")

    else :

        form = AvatarFormulario()

    return render(request, "AppCoder/agregarAvatar.html", {"formulario":form})