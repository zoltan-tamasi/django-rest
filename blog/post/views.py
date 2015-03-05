from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import authentication, permissions, viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer, UserSerializer
from .permissions import IsOwnerOrHasAuthority

class DefaultsMixin(object): 
	authentication_classes = (
 		authentication.BasicAuthentication,
 		authentication.TokenAuthentication,
 	)
	permission_classes = (
		permissions.IsAuthenticated,
		IsOwnerOrHasAuthority
 	)
	paginate_by = 25
	paginate_by_param = 'page_size'
	max_paginate_by = 100

class BlogPostViewSet(DefaultsMixin, viewsets.ModelViewSet):
	queryset = BlogPost.objects.order_by('date')
	serializer_class = BlogPostSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class UserViewSet(DefaultsMixin, viewsets.ModelViewSet):
	queryset = User.objects.order_by('id')
	serializer_class = UserSerializer

	

