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

# Importaciones para el Hack para ver las imagenes desde el admin
from django.conf import settings
from django.conf.urls.static import static


# from django.http import HttpResponse
# funcion que sirve como vista, migraremos la funcion a un archivo views
# def hello_world (request):
#     return HttpResponse('Hello-wold!')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', local_views.hello_world),

    # Con esta vista le mandamos un variable  de tipo GET como parametro que esta dentro del objeto request
    path('sorted/', local_views.sorted_numbers),

    # Mandamos 2 variables diferentes valores fuera del objeto request, para crear la vista se deben colocar los parametros de entrada del request, name y la edad por separado
    path('hi1/<str:name>/<int:edad>/', local_views.hi),
    path('posts/',post_views.list_posts),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Este es una extension para que podamos ver las imagenes guardadas desde el admin:
# el Media_Url: indica la path en el caso que fuera un archivo
# El Media_Root: Es una ruta que le damos para que nos los guarde los archivos, aparte de los que ya tienen 