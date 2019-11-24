from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

#Exceptions
from django.db.utils import IntegrityError
#Models
from django.contrib.auth.models import User
from users.models import Profile

#Forms
from users.forms import ProfileForm, SignupForm
@login_required
def update_profile(request):
    profile= request.user.profile
    if request.method =='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            data=form.cleaned_data
            profile.website=data['website']
            profile.biography=data['biography']
            profile.phone_number=data['phone_number']
            profile.picture = data['picture']
            profile.save()
            # el metodo cleaned_data nos trae un diccionario con campos ya validados.
            return redirect('update_profile')
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
            return redirect('feed')
        else:
            return render(request,'users/login.html',{'error':'Usuario y contaseña inválidos'})
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save() # Este metodo lo creamos como una nueva funcion que se encargara de guardarlo en la base de datos
            return redirect('login')
    else:
        form= SignupForm()
    return render(request=request,template_name='users/signup.html',context={
        'form':form
    })