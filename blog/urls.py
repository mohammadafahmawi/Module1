from django.urls import path

from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import PostViewSet,get_posts

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
urlpatterns =[
    path('posts/get_post/', get_posts, name='get_posts'),
]
urlpatterns += router.urls
