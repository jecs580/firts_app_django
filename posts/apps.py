# Declara toda nuestra configuracion de nuestra app hacia el publico en caso de que nuestra app sea reutilizable

from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'posts'
    varbose_name='Posts'