from rest_framework.routers import DefaultRouter
from .views import CommentModelViewSet

router = DefaultRouter()
router.register(r"comment", CommentModelViewSet, basename="comment")

urlpatterns = router.urls
