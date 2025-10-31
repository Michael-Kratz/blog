from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    context_object_name = "posts"

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "detailed"