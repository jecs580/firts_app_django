"""Post Urls"""
# Django
from django.urls import path

# Views
from posts import views
urlpatterns =[
    # Paths que estan relacionados con los posts
    path(route='',view=views.list_posts,name='feed'),
    path('posts/new/', views.create_post, name='create'), 
    # tienes 2 formas de crear un path, colocando los nombres de cada variable que envias, o no colando ningun nombre de variable en la ruta y la vista. Tú eliges
]