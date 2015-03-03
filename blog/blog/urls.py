from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/token/' , obtain_auth_token, name='api-token' ),
)
