from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, DraftPostListView, ArchivedPostListView

urlpatterns = [
    path("", PostListView.as_view(), name="post"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("new/", PostCreateView.as_view(), name="post_create"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name="post_edit"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),
    path("arcived/", ArchivedPostListView.as_view(), name="archived_list"),
    path("draft/", DraftPostListView.as_view(), name="draft_list"),
]