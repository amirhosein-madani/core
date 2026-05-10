from django.urls import reverse_lazy , reverse
from django.views.generic import (
    TemplateView,
    RedirectView,
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
)
from .models import Post
from accounts.mixins import LoginRequiredMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import math
# Create your views here.


class IndesxVIew(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        return context


class MaktabView(RedirectView):
    """
    this is a view to redirect to other urls
    """

    # url = "https://maktabkhooneh.org/"
    pattern_name = "index"


class PostListView(ListView):
    model = Post
    # queryset = Post.objects.all()
    context_object_name = "posts"
    template_name = "post_list.html"
    paginate_by = 4
    ordering = "id"
    # def get_queryset(self):
    #     posts =  Post.objects.filter(is_active = True)
    #     return posts



class PostListApiView(TemplateView):
    template_name = 'post_list_api.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        page = int(self.request.GET.get('page', 1))
        url = f'http://localhost:8000/blog/api/v1/post/?page={page}'
        
        try:
            response = requests.get(url, timeout=5)
            data = response.json()
            
            per_page = len(data['results'])
            total_pages = math.ceil(data['count'] / per_page)
            current_page = page
            
            context['posts'] = data['results']
            context['total_count'] = data['count']
            context['current_page'] = current_page
            context['total_pages'] = total_pages
            
            start = max(1, current_page - 2)
            end = min(total_pages, current_page + 2)
            context['page_range'] = range(start, end + 1)
            
        except:
            context['posts'] = []
            context['error'] = 'خطا در دریافت داده از سرور'
        
        return context

class PostDetailView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "post_detail.html"


class CreatePostView(CreateView):
    model = Post
    fields = ["title", "content", "status", "published_date"]
    template_name = "create_post.html"
    # form_class = PostFOrm
    "it's better to use form_class than using fields "
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ["title", "content", "status", "published_date"]
    success_url = reverse_lazy("post_list")


class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("post_list")


class SelectToUpdateVIew(ListView):
    model = Post
    template_name = "select_to_update.html"
    context_object_name = "posts"


@api_view()
def api_test(request):
    return Response({"name": "amir"})
