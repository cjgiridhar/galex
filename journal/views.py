from django.shortcuts import render
from journal.models import Article
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import api_view, throttle_classes
from rest_framework_extensions.cache.decorators import (cache_response)
from django.views.decorators.cache import cache_page
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import APIException

class NotFound(APIException):
    status_code = 404
    default_detail = 'Sorry!! Not Found'

# Create your views here.

import logging
logger = logging.getLogger(__name__)

class ArticleList(generics.ListCreateAPIView):
    logger.info("/articles list API got called..")
    renderer_classes = (JSONRenderer, )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    logger.info("/articles detail API got called..")
    renderer_classes = (JSONRenderer, )
    throttle_classes([UserRateThrottle])
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#@cache_page(60 * 10)
def ArticleListPage(request):
    logger.info("/articles list page got called..")
    try:
        articles = Article.objects.all()
        for article in articles:
            article.hero_image = str(article.hero_image).split('/')[-1]
    except ObjectDoesNotExist as e:
        logger.error(e.message)
        raise Http404
    return render(request, 'journal/list.html', {'articles':articles})

#@cache_page(60 * 30)
def ArticleDetailPage(request, pk):
    logger.info("/articles details page got called for pk", pk)
    return render(request, 'journal/detail.html', {'article_id':pk} )
