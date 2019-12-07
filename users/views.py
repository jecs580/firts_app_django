from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

#Exceptions
from django.db.utils import IntegrityError
#Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

#Forms
from users.forms import ProfileForm, SignupForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

# cuando colocamos un modulo entre parentesis para una nueva clase signifca que la nueva clase heredara todos los metodos

# esta clase devolvera un objeto del tipo que estamos haciendo el queryset
class UserDetailView(DetailView):
    """Vista detallada de usuario"""
    template_name='users/detail.html'
    slug_field='username'  # Nombre de un campo por cual buscar
    slug_url_kwarg='username' # tiene que ser igual al route que pusimos en el path
    queryset=User.objects.all()  # Como su nombre dice, indicamos a partir de que conjunto datos traera los datos.
    context_object_name='user' # Nombre con el que el template recibira los datos. Es como enviarle una varible te tipo diccionario

    # traeremos los posts del usuario encontrado
    def get_context_data(self, **kwargs):
        # agregar a las publicación del usuario al contexto
        context = super().get_context_data(**kwargs)
        user= self.get_object()
        # Agregamos al contexto los datos de los posts de cada usuario y lo ordenamos de manera descendente
        context['posts']= Post.objects.filter(user=user).order_by('-created')
        return context

@login_required
def update_profile(request):
    profile= request.user.profile
    if request.method =='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            data=form.cleaned_data # el metodo cleaned_data nos trae un diccionario con campos ya validados.
            profile.website=data['website']
            profile.biography=data['biography']
            profile.phone_number=data['phone_number']
            profile.picture = data['picture']
            profile.save()
            url=reverse('users:detail',kwargs={'username':request.user.username})
            return redirect(url)
    else:
        form = ProfileForm()   
    return render(request, 'users/update_profile.html',context=
        {
        'profile':profile,
        'user':request.user,
        'form': form,
        }
    )
    
def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']  # El nombre del campo "username" tiene que igual al name de la input correspondiente del html 
        password = request.POST['password']

        user=authenticate(request,username=username,password=password) #Esto verificara si existe un user registrado en nuestra base de datos que coincida con los campos de username y password
        if user:
            login(request,user)
            return redirect('posts:feed')
        else:
            return render(request,'users/login.html',{'error':'Usuario y contaseña inválidos'})
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save() # Este metodo lo creamos como una nueva funcion que se encargara de guardarlo en la base de datos
            return redirect('users:login')
    else:
        form= SignupForm()
    return render(request=request,template_name='users/signup.html',
    context={'form':form}
    )