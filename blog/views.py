from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from  django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post
from .forms import PostForm
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
### Post
class Index(APIView):
    
    def get(self, request):
        posts = Post.objects.all().order_by('created_at')
        page  = request.GET.get('page', '1')
        paginator = Paginator(posts, 5)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        selected_category = request.GET.get('category')
        if selected_category:
            posts = Post.objects.filter(category=selected_category)
        else:
            posts = Post.objects.all()
        
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    





class Write(APIView):
    def get(self, request):
        serializer = PostSerializer()  # Serializer 인스턴스 생성
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)  # 요청 데이터로 Serializer 인스턴스 생성
        
        if serializer.is_valid():
            serializer.save(writer=request.user.username, address = request.user.profile.address)  # 현재 사용자 설정
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Update(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

class Delete(View):
    
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DetailView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


# 참여버튼
class Participants(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        action = request.data.get('action') # 'join' or 'cancel'
        if action == 'join':
            if post.join_number < post.target_number and request.user not in post.recruited_users.all():
                post.join_number += 1
                post.recruited_users.add(request.user)
                post.save()                
                serializer = PostSerializer(post)
                return Response(serializer.data)
            else:
                return Response({'error': 'Cannot join.'}, status=status.HTTP_400_BAD_REQUEST)
            
        elif action == 'cancel':
            if request.user in post.recruited_users.all():
                post.join_number -= 1
                post.recruited_users.remove(request.user)
                post.save()
                
                serializer = PostSerializer(post)
                return Response(serializer.data)
            else:
                return Response({'error': 'Cannot cancel join.'}, status=status.HTTP_400_BAD_REQUEST)

        
                        
        if post.join_number == post.target_number:
            post.is_compelete = True
            post.save()
        else:
            post.is_compelete = False
            post.save()
        return Response({'error': 'Invalid action.'}, status=status.HTTP_400_BAD_REQUEST)
    
