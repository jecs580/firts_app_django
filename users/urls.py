"""User Urls"""

# Django
from django.urls import path

# importacion para usar las vistas basadas en clases
from django.views.generic import TemplateView

# Views
from users import views

urlpatterns=[
    # primera vista basada en clases, que sera el detalle de un user
     path(route='<str:username>/',view=views.UserDetailView.as_view(), name='detail'),
    # path(route='<str:username>/',view=TemplateView.as_view(template_name='users/detail.html'), name='detail'),

         # Paths que estan relacionados con los users 
    path(route='login/' ,view=views.login_view,name='login'),
    path(route='logout/', view=views.logout_view,name='logout'),
    path(route='signup/',view=views.signup,name='signup'),
    path(route='me/profile/', view=views.update_profile, name='update'),
]