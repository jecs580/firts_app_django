"""Platzigram middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse # Importacion que nos permite traer una url apartir del nombre que le coloquemos, es de la misma forma que le mandamos en el redirect


class ProfileCompletionMiddleware:
    """Middleware para completar perfil.

    Asegúra de que cada usuario que interactúa con la plataforma tenga su foto de perfil y biografía.
    """

    def __init__(self, get_response):
        """Inicializando el Middleware"""
        self.get_response = get_response

    def __call__(self, request):
        """Código que se ejecutará para cada solicitud antes de que se llame a la vista."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')
        
        # Esta linea se cuando el usuariario sea anonimo, osea que no a iniciado sesion o no tiene una cuenta
        response = self.get_response(request)
        return response