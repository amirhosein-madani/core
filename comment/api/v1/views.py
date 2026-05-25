from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ...models import Comment
from .serializers import CommentListSerializer, CommentDetailSerializer
from .permissions import IsOwnerOrReadOnly
from .paginations import DefaultPagination


class CommentListGenericApiView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["post", "user"]


class CommentDetailGenericApiView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
