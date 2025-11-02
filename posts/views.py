from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Status
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class PostListView(ListView):
    template_name = "posts/list.html"
    # model = Post
    published_status = Status.objects.get(name="published")
    queryset = Post.objects.filter(status=published_status).order_by("created_on").reverse()
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        number = [1, 2, 3, 4, 5]
        flag = True
        context["number"] = number
        context["flag"] = flag
        print(context)
        return context
    
    

class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "detailed"

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post")

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            return self.request.user == post.author
        

class DraftPostListView(ListView):
    template_name = "posts/drafts.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_status = Status.objects.get(name="draft")
        context["draft_list"] = Post.objects.filter(status=draft_status).filter(author=self.request.user).order_by("created_on").reverse()
        return context

class ArchivedPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/archived.html"
    archived_status = Status.objects.get(name="archived")
    queryset = Post.objects.all().filter(status=archived_status).order_by("created_on").reverse()
    context_object_name = "archived_posts"
