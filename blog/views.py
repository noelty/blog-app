from rest_framework import permissions, viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
