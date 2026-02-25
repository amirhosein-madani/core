from rest_framework.response import Response
from rest_framework.decorators import api_view

data = {"id": 1 , "title" : "hello"}


@api_view()
def post_list(request):
    return Response("ok")


@api_view()
def post_detail(request , id):
    return Response(data)