# user > views.py
from django.shortcuts import render, redirect
from django.middleware.csrf import get_token

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView

from django.contrib.auth import get_user_model

from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer, LoginSerializer, ChangePasswordSerializer, User, DeleteUserSerializer, UserUpdateSerializer
from .renderers import UserJSONRenderer
from user.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

User = get_user_model()


# Create your views here.
# 회원가입
class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        user = request.data

        serializer = self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            response.set_cookie('csrftoken', get_token(request))
            return response
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 로그인
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        response = Response(serializer.data, status=status.HTTP_200_OK)
        response.set_cookie('csrftoken', get_token(request))
        return response


# 토큰으로 유저 정보 반환
class UserCheckAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserUpdateSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response.set_cookie('csrftoken', get_token(request))
        return response


# 로그아웃
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        try:
            Token.objects.get(user_id=user.id).delete()
        except Token.DoesNotExist:
            return Response({'message': '유효하지 않는 유저정보 입니다.'}, status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_200_OK)


# 비밀번호 변경
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            current_password = serializer.validated_data.get(
                'current_password')
            new_password = serializer.validated_data.get('new_password1')

            if user.check_password(current_password):
                user.set_password(new_password)
                user.save()
                return Response({'message': '비밀번호 변경 성공'})
            else:
                return Response({'error': ['현재 암호가 올바르지 않습니다.']}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 프로필 업데이트
class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserUpdateSerializer(User)

        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = UserUpdateSerializer(
            user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 유저 삭제
class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = DeleteUserSerializer(data=request.data)

        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            if user.check_password(password):
                user.is_active = False
                user.save()
                return Response(status=status.HTTP_200_OK)

        return Response('유효하지 않은 유저정보 입니다.', status=status.HTTP_401_UNAUTHORIZED)
