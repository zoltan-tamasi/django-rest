from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'blogposts', views.BlogPostViewSet)
router.register(r'users', views.UserViewSet)