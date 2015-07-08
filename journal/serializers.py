__author__ = 'cgiridhar'
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from models import Article
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Article
        fields = ('id', 'title', 'pub_date', 'category', 'body', 'author')


class UserSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'articles',)