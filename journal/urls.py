__author__ = 'cgiridhar'

from django.conf.urls import url
from journal import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/articles/$', views.ArticleList.as_view()),
    url(r'^api/articles/(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view()),

    url(r'^api/users/$', views.UserList.as_view(),),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), ),

    url(r'^articles/$', views.index),
]

urlpatterns = format_suffix_patterns(urlpatterns)