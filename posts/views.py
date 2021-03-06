# Modulo para el manejo de respuestas diferente al HttpResponses
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Utilidades
from datetime import datetime

# Class View
from django.views.generic import ListView, DetailView,CreateView

# Mixins
from django.contrib.auth.mixins import LoginRequiredMixin
#form
from posts.forms import PostForm
from posts.models import Post

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

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    slug_url_kwarg='pk'
    queryset = Post.objects.all() # Hara un query con
    context_object_name = 'post'

class PostsFeedView(LoginRequiredMixin,ListView):
    """Retorna todos los posts publicados"""
    template_name = 'posts/feed.html'
    model = Post
    ordering=('-created',)
    paginate_by = 30
    context_object_name ='value' #Nombre del valor con el que se recibira en el template(html designado)

# @login_required
# def list_posts(request):
#     # contenido=[]
#     # for post in posts:
#     #     contenido.append("""
#     #     <h1><strong>{name}</strong></h1>
#     #     <p>{user} -<i>{timestamp}</i></p>
#     #     <figure><img src="{picture}"/></figure>
#     #     """.format(**post))
#     # return HttpResponse('<br>'.join(contenido))

#     # Retornamos render con parametros la request, un archivo template que se crea dentro de la aplicacion y datos la tabla. Nota no es necesario darle la ruta del archivo template puesto que el archivo settings lo buscara por todas las aplicaciones que tiene
#     posts = Post.objects.all().order_by('-created')
#     return(render(request,'posts/feed.html',{'value':posts})) # Se agrego el "posts/"" cuando se utiliza templates q se comparte entre apliaciones y no solo el template por aplicacione de django. Si no definiste el template general en los settings y no tienes la carpeta al mismo nivel de las aplicaciones, debes usar los templates por aplicacion.

class CreatePostView(LoginRequiredMixin,CreateView):
    """Creacion de un nuevo post"""
    template_name='posts/new.html'
    form_class= PostForm
    success_url=reverse_lazy('posts:feed') # Para las vistas basadas en clases es recomendable usar el reverse_lazy para no tener errores (Lo evalua hasta que lo necesite)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user']=self.request.user
        context['profile']=self.request.user.profile
        return context
# @login_required
# def create_post(request):
#     """Create new post view."""
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:feed')
#     else:
#         form = PostForm()
#     return render(
#         request=request,
#         template_name='posts/new.html',
#         context={
#             'form': form,
#             'user': request.user,
#             'profile': request.user.profile
#         }
#     )

