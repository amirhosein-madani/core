# from rest_framework.response import Response
# from rest_framework.decorators import api_view , permission_classes
# from rest_framework.views import APIView
# from django.shortcuts import get_object_or_404
# from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination

# @api_view(["GET","POST"])
# @permission_classes([IsAuthenticated])
# def post_list(request):

#     if request.method == "GET":
#         post = Post.objects.all()
#         serializers = PostSerializer(post, many =  True)
#         return Response(serializers.data)

#     elif request.method == "POST":

#         serializers = PostSerializer(data= request.data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response (serializers.data)


# @api_view(["GET" , "PUT" , "DELETE"])
# def post_detail(request , id):


#   post = get_object_or_404(Post , id = id)

#   if request.method == "GET":
#         serializers = PostSerializer(post)
#         return Response(serializers.data)

#   elif request.method == "PUT":

#         serializers = PostSerializer(post,data= request.data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response (serializers.data)

#   elif request.method == "DELETE":
#         post.delete()
#         return Response({"detail": "item removed successfully"} ,
#         status = status.HTTP_204_NO_CONTENT)


# ""
# class PostListView(APIView):
#       '''
#             getting a list of posts and create posts
#       '''
#       permission_classes = [IsAuthenticatedOrReadOnly]
#       serializer_class = PostSerializer
#       def get(self , request):
#             '''
#                investing a  list of posts
#             '''
#             post = Post.objects.all()
#             serializers = PostSerializer(post , many = True)
#             return Response(serializers.data)

#       def post(self , request):
#              '''
#              creating post with provided data
#              '''
#              serializers = PostSerializer(data= request.data)
#              serializers.is_valid(raise_exception=True)
#              serializers.save()
#              return Response(serializers.data)


# class PostDetailView(APIView):
#       """
#       detail of the post and edit and removing it.
#       """

#       permission_classes = [IsAuthenticated]
#       serializer_class = PostSerializer

#       def get(self , request , id ):
#             '''
#             show data of the post
#             '''
#             post = get_object_or_404(Post,id = id)
#             serializers = self.serializer_class(post)
#             return Response(serializers.data)

#       def post(self , request, id ):
#              '''
#              updata detail of the post data
#              '''
#              post = get_object_or_404(Post,id = id)
#              serializers = self.serializer_class(post,data= request.data)
#              serializers.is_valid(raise_exception=True)
#              serializers.save()
#              return Response(serializers.data)

#       def delete(self , request , id):
#              '''
#             delete the post
#              '''
#              post = get_object_or_404(Post,id = id)
#              post.delete()
#              return Response({"detail": "item removed successfully"} ,
#              status = status.HTTP_204_NO_CONTENT)


class PostListView(ListCreateAPIView):
    """
    getting a list of posts and create posts
    """

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailView(RetrieveUpdateDestroyAPIView):
    """
    detail of the post and edit and removing it.
    """

    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    lookup_field = "id"


class PostModelViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
        IsAdminOrReadOnly,
    ]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {"category": ["exact"], "author": ["in"]}
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination
    #  = $ @


class CategoryModelViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    serializer_class = CategorySerializer


# class ProductFilter(filters.FilterSet):
#     min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
#     max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

#     class Meta:
#         model = Product
#         fields = ['category', 'in_stock']
