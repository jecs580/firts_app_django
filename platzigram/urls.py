"""platzigram URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from platzigram import views as local_views
from posts import views as post_views
from users import views as users_views
# Import para hacer el hack de ver las imagenes desde el admin
from django.conf.urls.static import static
from django.conf import settings

'''Lo que hace es: Le suma a urlpatterns  una URL estatica con el valor de la media que tenemos y donde estamos parados en la media'''

# from django.http import HttpResponse
# funcion que sirve como vista, migraremos la funcion a un archivo views
# def hello_world (request):
#     return HttpResponse('Hello-wold!')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', local_views.hello_world, name='hello_world'),

    # Con esta vista le mandamos un variable  de tipo GET como parametro que esta dentro del objeto request
    path('sorted/', local_views.sorted_numbers,name='sort'),

    # Mandamos 2 variables diferentes valores fuera del objeto request, para crear la vista se deben colocar los parametros de entrada del request, name y la edad por separado
    path('hi1/<str:name>/<int:edad>/', local_views.hi),
    path('posts/',post_views.list_posts,name='feed'),
    path('users/login/',users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view,name='logout'),
    path('users/signup/',users_views.signup,name='signup'),
    path('users/me/profile/', users_views.update_profile, name='update_profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Este es una extension para que podamos ver las imagenes guardadas desde el admin:
# el Media_Url: indica la path en el caso que fuera un archivo
# El Media_Root: Es una ruta que le damos para que nos los guarde los archivos, aparte de los que ya tienen 
