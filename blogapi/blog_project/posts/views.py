from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer

# generics.ListAPIView

class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class PostList(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticated,) #adding authentication to our views
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) #only authenticated user can perform update operations
    # permission_classes = (permissions.IsAuthenticated,) #adding authentication to our views
    queryset = Post.objects.all()
    serializer_class = PostSerializer