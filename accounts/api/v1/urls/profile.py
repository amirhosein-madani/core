from django.urls import path
from ..views import *

urlpatterns = [

# profile
   path('profile/' , ProfileApiView.as_view() , name = 'user_profile')

]
