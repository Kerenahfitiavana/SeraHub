from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from .models import Comment
from .serializers import CommentSerializer

class CommnentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)