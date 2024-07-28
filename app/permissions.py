from rest_framework.permissions import BasePermission

class SoloAdministrador(BasePermission):
    message = 'Solo ADMIN puede accer a estas rutas'
    def has_permission(self, request, view):
        tipo = request.user.tipo
        if tipo == 'ADMIN':
            return True
        
        else:
            return False