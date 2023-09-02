from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, Comment, HashTag
from chat.models import ChatRoomJoin
from .forms import PostForm, CommentForm, HashTagForm
from group_buying_service.utils.paginator import get_page_data
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
        # posts = Post.objects.all().order_by('created_at')
        page  = request.GET.get('page', '')
        selected_category = request.GET.get('category')
        if selected_category:
            posts = Post.objects.filter(category=selected_category).order_by('created_at')
        else:
            posts = Post.objects.all().order_by('created_at')
        paginator = Paginator(posts, 10)  # 페이지당 10개씩 보여주기
        try:
            page_object = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            page_object = paginator.page(page)
        except EmptyPage:
            if page <= 0:
                page = 1
                page_object = paginator.page(page)
            else:
                page = paginator.num_pages
                page_object = paginator.page(page)
        
        serializer = PostSerializer(page_object, many=True)
        page_data = get_page_data(page, len(paginator.page_range))

        return Response({'posts': serializer.data, 'paginator': page_data}, status=status.HTTP_200_OK)


class Write(APIView):
    def get(self, request):
        serializer = PostSerializer()  # Serializer 인스턴스 생성
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)  # 요청 데이터로 Serializer 인스턴스 생성
        if serializer.is_valid():
            serializer.save(writer=request.user)  # 현재 사용자 설정
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Update(APIView):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            chatroom = post.chatroom
            is_joined = ChatRoomJoin.objects.filter(chatroom=chatroom, user=request.user, is_deleted=False).exists()
            return Response({**serializer.data, 'is_joined':is_joined})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Delete(APIView):

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response('삭제되었습니다.', status=status.HTTP_204_NO_CONTENT)


class DetailView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        chatroom = post.chatroom
        is_joined = ChatRoomJoin.objects.filter(chatroom=chatroom, user=request.user, is_deleted=False).exists()
        return Response({**serializer.data, 'is_joined':is_joined})


# 참여버튼
class Participants(View):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        action = request.data.get('action') # 'join' or 'cancel'
        if action == 'join':
            if post.join_number < post.target_number and request.user not in post.recruited_users.all():
                post.join_number += 1
                post.recruited_users.add(request.user)
                post.save()
                
                if post.join_number == post.target_number:
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
    
# # 참여버튼
# class Participants(View):
    
#     def post(self, request, pk):
#         post = get_object_or_404(Post, pk=pk)
            
#         if request.user in post.recruited_users.all():
#                 # 이미 모집한 사용자라면 아무 동작도 하지 않음
#             pass
#         else:
#             if post.join_number < post.target_number:
#                 post.join_number += 1
#                 post.recruited_users.add(request.user)
#                 post.save()

#         return redirect('blog:detail', pk=pk)


# 댓글
class CommentWrite(LoginRequiredMixin, View):

    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, pk=pk)

        if form.is_valid():
            content = form.cleaned_data['content']
            writer = request.user

            try:
                comment = Comment.objects.create(post=post, content=content, writer=writer)
            except ObjectDoesNotExist as e:
                print('Post does not exist.', str(e))
            except ValidationError as e:
                print('Valdation error occurred', str(e))
            
            return redirect('blog:detail', pk=pk)
        
        hashtag_form = HashTagForm()
        
        context = {
            "title": "Blog",
            'post_id': pk,
            'comments': post.comment_set.all(),
            'hashtags': post.hashtag_set.all(),
            'comment_form': form,
            'hashtag_form': hashtag_form
        }
        return render(request, 'blog/post_detail.html', context)


class CommentDelete(View):
    
    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        
        post_id = comment.post.id

        comment.delete()
        
        return redirect('blog:detail', pk=post_id)


#태그
class HashTagWrite(LoginRequiredMixin, View):
    
    def post(self, request, pk):
        form = HashTagForm(request.POST)
        
        post = get_object_or_404(Post, pk=pk)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            writer = request.user

            try:
                hashtag = HashTag.objects.create(post=post, name=name, writer=writer)
            except ObjectDoesNotExist as e:
                print('Post does not exist.', str(e))
            except ValidationError as e:
                print('Valdation error occurred', str(e))

            return redirect('blog:detail', pk=pk)

        comment_form = CommentForm()
        
        context = {
            'title': 'Blog',
            'post': post,
            'comments': post.comment_set.all(),
            'hashtags': post.hashtag_set.all(),
            'comment_form': comment_form,
            'hashtag_form': form
        }
        
        return render(request, 'blog/post_detail.html', context)


class HashTagDelete(View):
    
    def post(self, request, pk):
        hashtag = get_object_or_404(HashTag, pk=pk)
        post_id = hashtag.post.id

        hashtag.delete()
        
        return redirect('blog:detail', pk=post_id)