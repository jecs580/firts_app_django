'''Modulo para que nuestro archivo interactue con el ORM'''
from django.db import models
# Aqui definimos los modelos de nuestros datos
class user(models.Model):
    '''User model'''
    # Por defecto django ya agrega un id a nuestra tabla

    # Almacena correos. Con el parametro "unique" definimos que los correos sean unicos, no se permitiran 2 o mas emails duplicados
    email=models.EmailField(unique=True)

    #Almacena texto, estos campos necesitan definirse una maximo longitud
    password=models.CharField(max_length=100)
    firts_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    #Almacena booleanos. Se debe establecer el valor por defecto sino da error
    is_admin=models.BooleanField(default=False)

    # El textfield() puede introducir mayor cantidad de texto que un charfield()
        # blank: Para consultar si el campo puede estar vacio o no
    bio=models.TextField(blank=True)

    # Almacena la fecha
    birthdate=models.DateField(blank=True,null=True)

    # Almacena la fecha y hora
        # auto_now_add: Almacena los datos cuando se creo el campo
    created=models.DateTimeField(auto_now_add=True)
        # auto_now: Almacena los datos cuando se modifico por ultima vez
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):      
        return self.email

