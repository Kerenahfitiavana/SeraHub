from rest_framework import serializers
from comments.serializers import CommentSerializer
from . models import Post

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'content', 'post_image', 'category', 'post_date', 'comments')
        
