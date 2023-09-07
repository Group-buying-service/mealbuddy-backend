from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post
from chat.models import ChatRoomJoin
from mealbuddy.utils.paginator import get_page_data
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer


### Post
class Index(APIView):
    
    def get(self, request):

        page = request.GET.get('page', 1)
        selected_category = request.GET.get('category')
        user = request.user
        user_address = user.address       
        queryset = Post.objects.filter(address=user_address) # 동일한 주소를 가진 게시글 필터링

        if selected_category:
            posts = queryset.filter(category=selected_category).order_by('-created_at')
        else:
            posts = queryset.order_by('-created_at')
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
        page_data = get_page_data(int(page), len(paginator.page_range))

        return Response({'posts': serializer.data, 'paginator': page_data}, status=status.HTTP_200_OK)


class Write(APIView):

    def get(self, request):
        serializer = PostSerializer()  # Serializer 인스턴스 생성
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)  # 요청 데이터로 Serializer 인스턴스 생성
        if serializer.is_valid():
            serializer.save(writer=request.user, address = request.user.address)  # 현재 사용자 설정
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Update(APIView):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, pk):
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
