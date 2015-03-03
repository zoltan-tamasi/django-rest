from django.shortcuts import render
from rest_framework import authentication, permissions, viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer

class DefaultsMixin(object): 
	authentication_classes = (
 		authentication.BasicAuthentication,
 		authentication.TokenAuthentication,
 	)
	permission_classes = (
		permissions. IsAuthenticated,
 	)
	paginate_by = 25
	paginate_by_param = 'page_size'
	max_paginate_by = 100

class BlogPostViewSet(DefaultsMixin, viewsets.ModelViewSet):
	queryset = BlogPost.objects.order_by('date')
	serializer_class = BlogPostSerializer

