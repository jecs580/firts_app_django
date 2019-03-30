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
from platzigram import views
# from django.http import HttpResponse
# funcion que sirve como vista, migraremos la funcion a un archivo views
# def hello_world (request):
#     return HttpResponse('Hello-wold!')
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello-world/',views.hello_world),
    path('sorted/',views.sorted_numbers),
    path('hi/<str:name>/<int:edad>/',views.hi)
]
