from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
    })


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

"""
class SnippetHighlight(generics.GenericAPIView):
queryset = Snippet.objects.all()
render_classes = (renderers.StaticHTMLRenderer,)

def get(self, request, *args, **kwargs):
    snippet = self.get_object()
    return Response(snippet.highlighted)


class SnippetList(generics.ListCreateAPIView):
"""
#List all code snippets, or create a new snippet.
"""
queryset = Snippet.objects.all()
serializer_class = SnippetSerializer
permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
queryset = Snippet.objects.all()
serializer_class = SnippetSerializer
permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly,)
"""

"""
class UserList(generics.ListAPIView):
queryset = User.objects.all()
serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
queryset = User.objects.all()
serializer_class = UserSerializer
"""


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer