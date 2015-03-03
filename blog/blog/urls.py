from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from post.urls import router

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/token/', obtain_auth_token, name='api-token'),

 	url(r'^api/', include(router.urls)),
)

