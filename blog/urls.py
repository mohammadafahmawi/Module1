from django.urls import path
from rest_framework import routers

from ai_content.service.summarize import summarize_post
from .views import PostViewSet, get_posts, generate_post

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
urlpatterns =[
    path('posts/get_post/', get_posts, name='get_posts'),
    path('posts/generate/', generate_post, name='generate_post' ),
    path("posts/summarize/", summarize_post, name='summarize_post'),
]
urlpatterns += router.urls
