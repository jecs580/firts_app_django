"""User Urls"""

# Django
from django.urls import path

# importacion para usar las vistas basadas en clases
from django.views.generic import TemplateView

# Views
from users import views

urlpatterns=[
    # primera vista basada en clases, que sera el detalle de un user
    path(route='<str:username>/',view=TemplateView.as_view(template_name='users/detail'), name='detail'),

 # Paths que estan relacionados con los users 
    path('users/login/',views.login_view, name='login'),
    path('users/logout/', views.logout_view,name='logout'),
    path('users/signup/',views.signup,name='signup'),
    path('users/me/profile/', views.update_profile, name='update_profile'),
]