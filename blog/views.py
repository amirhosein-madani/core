from django.shortcuts import render
from django.views.generic import  TemplateView , RedirectView , ListView
from .models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

class IndesxVIew(TemplateView):
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
    

class ProductListView(ListView):
    model = Post
    # queryset = Post.objects.all()
    context_object_name = "posts"
    template_name = "post_list.html"
    paginate_by = 4
    ordering = "id"
    # def get_queryset(self):
    #     posts =  Post.objects.filter(is_active = True)
    #     return posts

@api_view()
def api_test(request):
    return Response ({"name": "amir"})
    