from django.urls import path , include
from  .views import *

urlpatterns = [
    path("login/", user_login , name = "login"),
    path("logout/" , user_logout , name = "logout"),
    path('api/v1/' , include('accounts.api.v1.urls'))
]
