from django.urls import path
from  .views import IndesxVIew , MaktabView , ProductListView , api_test

urlpatterns = [
    path("index/" , IndesxVIew.as_view( extra_context = {"name": "amir "}) , name= "index" ),
    path("maktab" ,MaktabView.as_view() , name="maktab" ),
    path("product-list/", ProductListView.as_view() , name= "product_list"),
    path("api/" , api_test , name="api_test"),
]
