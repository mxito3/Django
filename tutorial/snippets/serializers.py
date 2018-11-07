from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # owner字段必须要有，因为Snippet里面没有owner字段

    class Meta:
        model = Snippet
        # fields里面是需要序列化的字段，得把owner加进去
        fields = ('id', 'title', 'code', 'linenos',
                  'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
        # snippets指的是user创建的snippets
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
