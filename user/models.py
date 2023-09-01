# group_buying_service > user > models.py
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import BooleanField

from .managers import UserManager
from core.models import TimestampedModel


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    
    username = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username
    

    # token 생성 함수
    @property
    def token(self): # user.token
        return self._generate_jwt_token( )

    def _generate_jwt_token(self):
        dt = datetime.now( ) + timedelta(days=1) # days=1 / 토큰 만료 기간이 1일

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')

        return token


class Profile(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    address = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username
    