from django.conf.urls import include, url
from django.contrib import admin
from journal.views import index
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'drf_learn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('journal.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),

]