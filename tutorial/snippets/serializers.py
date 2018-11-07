from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # owner字段必须要有，因为Snippet里面没有owner字段
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        # fields里面是需要序列化的字段，得把owner加进去
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.ModelSerializer):
        # snippets指的是user创建的snippets
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
