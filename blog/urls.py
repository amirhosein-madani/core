from django.urls import path
from  .views import *

urlpatterns = [
    path("index/" , IndesxVIew.as_view( extra_context = {"name": "amir "}) , name= "index" ),
    path("maktab" ,MaktabView.as_view() , name="maktab" ),
    path("post-list/", ProductListView.as_view() , name= "post_list"),
    path("api/" , api_test , name="api_test"),
    path("post_detail/<slug:slug>" , PostUpdateView.as_view() , name= "post_detail"),
    path("create_post/" , CreatePostView.as_view() , name= "create_post"),
    path("update_post/<slug:slug>/" , PostUpdateView.as_view() , name= "post_update"),
    path("delete_post/<slug:slug>/" , PostDeleteView.as_view() , name= "post_delete"),
    path("select_to_update/" , SelectToUpdateVIew.as_view() , name= "select_to_update")
    
]
