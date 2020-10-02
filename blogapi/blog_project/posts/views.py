from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model # new
from rest_framework import generics,viewsets
from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer,UserSerializer

# generics.ListAPIView


# class PostList(generics.ListCreateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# # class PostList(generics.ListAPIView):
# #     permission_classes = (permissions.IsAuthenticated,) #adding authentication to our views
# #     queryset = Post.objects.all()
# #     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,) #only authenticated user can perform update operations
#     # permission_classes = (permissions.IsAuthenticated,) #adding authentication to our views
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# '''
# User list class would list out all users
# '''
# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

'''
testing out viewsets
'''
class PostViewSet(viewsets.ModelViewSet):  #ModelViewset provides both ListVIew as well Detail View
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

