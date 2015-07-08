from django.shortcuts import render
from journal.models import Article
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

import logging
logger = logging.getLogger(__name__)

class ArticleList(generics.ListCreateAPIView):
    logger.info("/articles got called..")
    renderer_classes = (JSONRenderer, )
    queryset = Article.objects.filter()
    serializer_class = ArticleSerializer

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
    #
    # def get_queryset(self):
    #     #logger.info("SnippetList::get_queryset::" + self.request.user)
    #     return Article.objects.filter(author=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = (JSONRenderer, )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
    return render(request, 'journal/index.html')

