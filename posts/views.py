# Modulo para el manejo de respuestas diferente al HttpResponses
from django.shortcuts import render

# Utilidades
from datetime import datetime
# posts=[
#     {
#         'name':'Mont Blac',
#         'user':'Jorge Callisaya',
#         'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'picture':'https://picsum.photos/200/200/?image=1036',
#     },
#      {
#         'name': 'Via Láctea',
#         'user': 'C. Vander',
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'picture': 'https://picsum.photos/200/200/?image=903',
#     },
#     {
#         'name': 'Nuevo auditorio',
#         'user': 'Thespianartist',
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'picture': 'https://picsum.photos/200/200/?image=1076',
#     }
# ]
posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]
def list_posts(request):
    # contenido=[]
    # for post in posts:
    #     contenido.append("""
    #     <h1><strong>{name}</strong></h1>
    #     <p>{user} -<i>{timestamp}</i></p>
    #     <figure><img src="{picture}"/></figure>
    #     """.format(**post))
    # return HttpResponse('<br>'.join(contenido))

    # Retornamos render con parametros la request, un archivo template que se crea dentro de la aplicacion y datos la tabla. Nota no es necesario darle la ruta del archivo template puesto que el archivo settings lo buscara por todas las aplicaciones que tiene
    return(render(request,'posts/feed.html',{'value':posts})) # Se agrego el "posts/"" cuando se utiliza templates q se comparte entre apliaciones y no solo el template por aplicacione de django. Si no definiste el template general en los settings y no tienes la carpeta al mismo nivel de las aplicaciones, debes usar los templates por aplicacion.