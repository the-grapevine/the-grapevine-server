from django.urls import path

from posts import views


urlpatterns = [
    path('', views.PostListAPIView.as_view(), name='post-list'),
]
