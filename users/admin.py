#Django
from django.contrib import admin

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