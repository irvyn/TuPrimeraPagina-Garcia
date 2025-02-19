
from .models import UsuarioPerfil

def get_user(request):
    profile = UsuarioPerfil.objects.get(usuario=request.user)

    return {
        'id': request.user.id,
        'username': request.user.username,
        'avatar': profile.avatar.url if profile.avatar else '/media/avatars/empty-profile.png'
    }