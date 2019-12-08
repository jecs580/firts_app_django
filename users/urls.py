"""User Urls"""

# Django
from django.urls import path

# importacion para usar las vistas basadas en clases
from django.views.generic import TemplateView

# Views
from users import views

urlpatterns=[
   
         # Paths que estan relacionados con los users 
  
    path(route='logout/', view=views.logout_view, name='logout'),
      # path(route='login/' ,view=views.login_view, name='login'),
    path(route='login/' ,view=views.LoginView.as_view(), name='login'),
    # path(route='me/profile/', view=views.update_profile, name='update'),
    path(route='me/profile/', view=views.UpdateProfileView.as_view(), name='update'), # NOTA: Cuando tengas path con funciones y clases al mismo tiempo, asegurate de colocar primero las que son con funciones. De otro modo solo reconocera la de ClassViews y no las de funciones
     # primera vista basada en clases, que sera el detalle de un user

    # path(route='signup/', view=views.signup, name='signup'),    
    path(route='signup/', view=views.SignupView.as_view(), name='signup'),
   
    path(route='<str:username>/',view=views.UserDetailView.as_view(), name='detail'),
    # path(route='<str:username>/',view=TemplateView.as_view(template_name='users/detail.html'), name='detail'),

]