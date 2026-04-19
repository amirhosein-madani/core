from django.urls import path
# from rest_framework.authtoken.views import ObtainAuthToken

from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  , TokenVerifyView

urlpatterns = [
#  registeration
path('register/' , RegisterationAPIView.as_view() , name = 'register'),
# change password
path('change-password/' , ChangePasswordApiView.as_view() , name = 'change_password' ),
# reset password
# login token
path('token-login/', CustomObtainAuthToken.as_view() , name = 'token-login'),
path('token-logout/', CustomDiscardAuthToken.as_view() , name = 'token-logout'),
# activation
path("test/email/" , TestEmailApiVIew.as_view() , name = 'test-email'),
# path('activation/confrim/')
# resend activation
# path('activation/resend/')
# login jwt
path('jwt/create/' , CustomTokenObtainPairView.as_view() , name = 'jwt-create'),
path('jwt/refresh/' , TokenRefreshView.as_view() , name = 'jwt-refresh'),
path('jwt/verify/' , TokenVerifyView.as_view() , name = 'jwt-verify'),
# profile
path('profile/' , ProfileApiView.as_view() , name = 'user_profile')

]
