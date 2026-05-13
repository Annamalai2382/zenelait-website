from rest_framework import serializers, viewsets
from .models import Post, Category

class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    author_username = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'summary', 'content', 'category_name', 'author_username', 'created_at', 'thumbnail']

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer
