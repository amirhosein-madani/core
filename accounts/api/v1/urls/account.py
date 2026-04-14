from django.urls import path
from ..views import *
from rest_framework_simplejwt.views import  TokenRefreshView  , TokenVerifyView

urlpatterns = [
#  registeration
   path('register/' , RegisterationAPIView.as_view() , name = 'register'),


# change password
   path('change-password/' , ChangePasswordApiView.as_view() , name = 'change_password' ),
# reset password
# login token
   path('token-login/', CustomObtainAuthToken.as_view() , name = 'token-login'),
   path('token-logout/', CustomDiscardAuthToken.as_view() , name = 'token-logout'),

# login jwt
   path('jwt/create/' , CustomTokenObtainPairView.as_view() , name = 'jwt-create'),
   path('jwt/refresh/' , TokenRefreshView.as_view() , name = 'jwt-refresh'),
   path('jwt/verify/' , TokenVerifyView.as_view() , name = 'jwt-verify'),
]
