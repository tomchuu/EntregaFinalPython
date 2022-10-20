from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Avatar
class FormularioRutinas(forms.Form):

    nombre = forms.CharField()
    dias = forms.DateField()



class FormularioCliente(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    fechadeingreso = forms.DateField()



class FormularioGimnasio(forms.Form):

    nombre = forms.CharField()
    valoracion = forms.IntegerField()



class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]



class FormularioEditar(UserCreationForm):

    
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ["imagen"]