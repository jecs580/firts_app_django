from django.db import models

from django.contrib.auth.models import User
'''Existe otra forma para llamar al modelo sin necesidad de importarlo'''
#from users.models import Profile
'''Clase que se relaciona con User y con Profile mediante sus clave foraneas'''
class Post(models.Model):
    
    #Vinculamos los post con un user, al momento que se elimine el user tambien se eliminara sus post
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #Relacionamos profile para ahorrarnos tiempo al traer  los datos que del profile que sean necesarios
    profile=models.ForeignKey('users.Profile',on_delete=models.CASCADE) # Esta es otra forma de llamar a un modelo: primero el nombre de la aplicacion.nombre del modelo
    title=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='posts/photos')
    created=models.DateField(auto_now_add=True)
    modified=models.DateField(auto_now=True)

    def __str__(self):
        # Se puede modificar la forma de como nos devolvera las consultas, enviando una cadena 0-0
        return '{} por @{}'.format(self.title, self.user.username)