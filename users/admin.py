#Django
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Models
from users.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #Variable que sirve para ver los campos que nos mostrará de entrada en forma de lista de todos los regitros
    list_display=('id','user','phone_number','website','picture')
    
    # La variable nos permite acceder al detalle del perfil seleccionado dando click en user y su numero telefonico
    list_display_links=('id','user',)

    #para editar campos desde sin necesidad de entrar al detalle
    list_editable=('phone_number','website','picture')

    #Para tener un buscador en la aplicacion
    # OJO: Si quieres buscar por campos que son heredados se coloca la doble barra en lucar del punto
    search_fields=('user__email','user__username','user__first_name','user__last_name','phone_number')

    #Colocar filtros en las busquedas.
    # Si colocas created, modified django lo sobre-entiende que es un campo de fecha y mostrar muchas opciones de filtrado por fechas
    list_filter=('user__is_active','user__is_staff','created','modified')

    #Variable para que customiza el detalle de un elemento de tu aplicacion
    fieldsets=(
        (
            'Profile',{
                'fields':(('user','picture'),
                         )
            }
        ),
        (
            'Informacion Extra',{
                'fields':(('website','phone_number'),
                          ('biography'),
                         )
            }
        ),
        (
            'Metadata',{
               'fields':(('created','modified'),
                ),
            }
        )
    )
    # Como se lee en la variable, indica que campos seran de solo lectura
    readonly_fields =('created','modified',)

    #Configurando el profile para q aparesca su creacion al crear un user
class ProfileInline(admin.StackedInline):
    # modelo que queremos añadir
    model=Profile
    # no puede ser borrado
    can_delete=False
    # Nombre en plural cuando se de la categoria de nuestro modelo
    verbose_name_plural='Profilesss'

#Clase q sobre-escribe la clase que ya viene por defecto para el modelo
class UserAdmin(BaseUserAdmin):
    # Agregar el administrador de profile al administrador de usuario base
    inlines=(ProfileInline,)
    list_display=('pk','username','email','first_name','last_name','is_active','is_staff')
# Se des-registra del modelo de User para poder aplicar el mismo modelo pero con modificado enviandole el parametro del UserAdmin 
admin.site.unregister(User)
admin.site.register(User,UserAdmin)