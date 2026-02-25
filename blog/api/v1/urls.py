from .views import *
from django.urls import path

urlpatterns = [
    path("post_list/" , post_list , name = "api_post_list "),
    path("post_detail/<int:id>/" , post_detail , name = "api_post_detai"),
]
