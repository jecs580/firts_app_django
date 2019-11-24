# Django
from django import forms

#Models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    username=forms.CharField(min_length=4,max_length=50)
    password=forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation=forms.CharField(max_length=70, widget=forms.PasswordInput())
    first_name=forms.CharField(min_length=2,max_length=50)
    last_name=forms.CharField(min_length=2,max_length=50)
    email=forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput())

    def clean_username(self):
        """Funcion para validar que el nombre del usuario sea unico"""
        username=self.cleaned_data['username'] # Llamamos al dato, que ya fue limpiado con max, y min definidos anteriormente, y validados por djago.
        username_taken=User.objects.filter(username=username).exists() # Con el metod exists() nos devolvera un booleano.
        if username_taken:
            raise forms.ValidationError('El nombre de usuario ya esta en uso') # Con esto lanzamos nuestras propia validacion personalizada y lo mandamos como error.
        return username # Siempre que validez un campo en una funcion tienes que devolver el campo.
    def clean(self):
        """Verificando  que password coincida con password_confirmacion"""
        data =super().clean()# no queremos sobre-escribir todo el metodo que clean manda a llamar a otras cosas, por eso traemos los datos que ya nos traeria clean si no lo hubieramos sobre-escrito
        password=data['password']
        password_confirmation=data['password_confirmation']

        if password!= password_confirmation:
            raise forms.ValidationError('El password no coincide')
        return data
    def save(self):
        """Creacion de usuario y perfil en la DataBase"""
        data=self.cleaned_data # Primero traemos los del form
        data.pop('password_confirmation') # quitamos el dato de password confirmations que nos sirve con el modelo.
        user = User.objects.create_user(**data)
        profile=Profile(user=user)
        profile.save()
class ProfileForm(forms.Form):
    website=forms.URLField(max_length=200, required = True)
    biography=forms.CharField(max_length=500, required =False)
    phone_number=forms.CharField(max_length=20,required=False)
    picture=forms.ImageField()