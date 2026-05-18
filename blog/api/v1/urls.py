from .views import *

from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"post", PostModelViewSet, basename="post")
router.register(r"category", CategoryModelViewSet, basename="category")

# urlpatterns = [
# path("post_list/" , post_list , name = "api_post_list "),
# path("post_detail/<int:id>/" , post_detail , name = "api_post_detai"),
# path("post_list/" , PostListView.as_view() , name = "api_post_list "),
# path("post_detail/<int:id>/", PostDetailView.as_view() , name = "api_post_detai"),

# ]
urlpatterns = [path("gold/", TestApiView.as_view(), name="test_api_dollar")]

urlpatterns += router.urls
