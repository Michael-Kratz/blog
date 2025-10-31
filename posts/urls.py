from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="post"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="post_detail"),  
]