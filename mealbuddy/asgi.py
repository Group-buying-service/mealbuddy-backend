"""
ASGI config for mealbuddy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mealbuddy.settings")
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.contrib.auth import get_user_model
from user.backends import JWTAuthMiddleware
from chat.routing import websocket_urlpatterns as chat_urlpatterns
from notification.routing import websocket_urlpatterns as notification_urlpatterns

User = get_user_model()

application = ProtocolTypeRouter(
    {
        "https": django_asgi_app,
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            JWTAuthMiddleware(URLRouter(chat_urlpatterns + notification_urlpatterns))
        ),
    }
)