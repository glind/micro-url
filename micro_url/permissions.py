from rest_framework.permissions import IsAuthenticated


class AllowOptionsAuthentication(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return True

        if getattr(request, 'session', None) and \
                request.session.get('jwt_organization_uuid'):
            return True
        return False
