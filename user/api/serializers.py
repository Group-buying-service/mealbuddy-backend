from django.contrib.auth import authenticate
from django.utils import timezone

from rest_framework import serializers

from user.models import User

### Register
class RegistrationSerializer(serializers.ModelSerializer):
    
    # password 최소 8자 ~ 최대 128자
    password = serializers.CharField(
        max_length = 128,
        min_length = 8,
        write_only = True 
    )
    
    token = serializers.CharField(max_length=255, read_only=True)
    
    class Meta:
        model = User
        fields = [
            'username',
            'email', 
            'password',
            'token'
            ]
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


### Login
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    last_login = serializers.CharField(max_length=255, read_only=True)
    
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        
        user = authenticate(username=email, password=password)
        
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found'
            )
        
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])
        
        return {
            'email': user.email,
            'username': user.username,
            'last_login': user.last_login
        }
    

### UserDetail
class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
            'token'
        ]
        
        read_only_fields = ('token', )
        
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        
        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance