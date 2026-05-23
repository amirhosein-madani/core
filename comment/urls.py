from django.urls import path , include


urlpatterns = [
    path('api/v1/' , include('comment.api.v1.urls'))
]
