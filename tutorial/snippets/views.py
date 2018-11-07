from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import renderers


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # permission_classes用来限制权限
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    # 存入模型前存入user

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        # 返回的是用用户建立snippet实例时选择的render方式渲染的html(序列化后)

        return Response(snippet.highlighted)


@api_view(['GET'])
def api_root(request, format=None):
        # reverse返回完全编码的url格式，第一个参数是url name
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
