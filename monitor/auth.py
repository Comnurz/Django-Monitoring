from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from monitor.models import ServerToken


class ServerTokenAuthentication(BaseAuthentication):
    keyword = 'Token'

    def authenticate(self, request):
        header = request.META.get('HTTP_AUTHORIZATION', '')
        parts = header.split()
        if len(parts) != 2 or parts[0] != self.keyword:
            return None
        try:
            token = ServerToken.objects.select_related('server').get(key=parts[1])
        except ServerToken.DoesNotExist:
            raise AuthenticationFailed('Invalid token.')
        server = token.server
        try:
            server_user = server.serveruser_set.first()
            user = server_user.user_id.first() if server_user else None
        except Exception:
            user = None
        return (user, server)

    def authenticate_header(self, request):
        return self.keyword
