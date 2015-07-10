__author__ = 'cgiridhar'

from django.conf.urls import url
from journal import views
from rest_framework.urlpatterns import format_suffix_patterns
from gale import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^api/articles/$', views.ArticleList.as_view()),
    url(r'^api/articles/(?P<pk>[0-9]+)/$',views.ArticleDetail.as_view()),

    url(r'^api/users/$', views.UserList.as_view(),),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), ),

    url(r'^$', views.ArticleListPage),
    url(r'^articles/(?P<pk>[0-9]+)/$', views.ArticleDetailPage),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)