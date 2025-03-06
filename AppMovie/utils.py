from .models import UsuarioPerfil

import logging

logger = logging.getLogger(__name__)

def get_user(request):
    default_response = {
        'id': -1,
        'username': 'Unknown',
        'avatar': '/media/avatars/empty-profile.png',
        'error': 'User profile does not exist.'
    }

    try:
        profile = UsuarioPerfil.objects.get(usuario=request.user)
        return {
            'id': request.user.id,
            'username': request.user.username,
            'avatar': profile.avatar.url if profile.avatar else '/media/avatars/empty-profile.png'
        }
    except UsuarioPerfil.DoesNotExist:
        logger.warning(f'User profile for user {request.user.username} does not exist.')
    except UsuarioPerfil.MultipleObjectsReturned:
        default_response['error'] = 'Multiple profiles found for the user.'
    except AttributeError:
        default_response['error'] = 'Attribute error occurred.'
    except ValueError:
        default_response['error'] = 'Value error occurred.'
    except Exception as e:
        default_response['error'] = f'An unexpected error occurred: {str(e)}'

    return default_response