# una forma diferente con el manejo de forms usando los models.
#django
from django import forms

#Models
from posts.models import Post

class PostForm(forms.ModelForm): # recuerda que debes llamar "forms.ModelForm" y no "forms.Form"
    class Meta:
        '''Configuracion del formulario'''
        model=Post
        fields=('user','profile','title','photo') # Ya no definimos nuevamente los campos, sino llamanos con que nombre estaban el archivo model