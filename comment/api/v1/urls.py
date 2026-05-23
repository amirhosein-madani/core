from rest_framework.routers import DefaultRouter
from .views import CommentListGenericApiView , CommentDetailGenericApiView
from django.urls import path
# router = DefaultRouter()
# router.register(r"comment", CommentModelViewSet, basename="comment")

# urlpatterns = router.urls
urlpatterns = [
    path('comment/' ,CommentListGenericApiView.as_view() , name = 'comment-list'),
    path('comment/<int:pk>/' ,CommentDetailGenericApiView.as_view() , name = 'comment-detail')

]

