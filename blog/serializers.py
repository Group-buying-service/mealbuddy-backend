from rest_framework import serializers, viewsets
from .models import Post
# Serializer 정의
class PostSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='writer.profile.address', read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

# ViewSet 정의
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer






