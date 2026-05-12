from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from helloworld.serializers import PostSerializer
from helloworld.models import Post
from helloworld.permissions import IsPostPossessor
from helloworld.filters import PostFilter

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class HelloWorldView(APIView):

    def get(self, request):
        return Response({'message': 'Hello world!'})


class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter , filters.OrderingFilter]
    filterset_class = PostFilter
    ordering_fields = ['id']

    search_fields = ['title', 'content']

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)