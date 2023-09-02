"""
ASGI config for group_buying_service project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import jwt

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.middleware import BaseMiddleware
from channels.security.websocket import AllowedHostsOriginValidator
from channels.db import database_sync_to_async
from django.core.asgi import get_asgi_application
from django.contrib.auth import get_user_model
from django.conf import settings

from chat.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "group_buying_service.settings")

django_asgi_app = get_asgi_application()

User = get_user_model()


class JWTAuthMiddleware(BaseMiddleware):

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        # JWT 검증
        jwt_token = self.get_jwt_token_from_scope(scope)
        user = await self.get_user_from_jwt(jwt_token)
        scope["user"] = user
        return await super().__call__(scope, receive, send)

    def get_jwt_token_from_scope(self, scope):
        query_string = scope.get("query_string", b"").decode("utf-8")
        parts = query_string.split("=")
        if len(parts) > 1:
            return parts[1]
        return ""

    @database_sync_to_async
    def get_user_from_jwt(self, token):
        decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = decoded_payload["id"]
        return User.objects.get(id=user_id)


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        # "websocket": AllowedHostsOriginValidator(
        #     AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        # ),
        "websocket": AllowedHostsOriginValidator(
            JWTAuthMiddleware(URLRouter(websocket_urlpatterns))
        ),
    }
)