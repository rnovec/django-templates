from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    # viewset fields
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # django filters fields
    filterset_fields = '__all__'
    search_fields = ['description', 'title']
    ordering_fields = '__all__'
    ordering = ['-created_at']
