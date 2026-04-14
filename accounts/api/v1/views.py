from rest_framework import   status
from rest_framework.permissions import  IsAuthenticated
from blog.api.v1.permissions import IsNotAuthenticated
from rest_framework.generics import GenericAPIView , RetrieveUpdateAPIView
from .serializers import RegisterationSerializer , CustomTokenObtainPairSerializer , ChangePasswordSerializer , ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from ...models import Profile
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterationAPIView(GenericAPIView):
    '''
        this is a view for register a user 
    '''
    serializer_class = RegisterationSerializer
    permission_classes = [IsNotAuthenticated]

    def post(self , request):

        serializer = self.serializer_class(data= request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        data = {'username' : serializer.validated_data['username']}
        return Response(data ,status= status.HTTP_201_CREATED )


class CustomObtainAuthToken(ObtainAuthToken):

    '''
    this is a views to create a auth_token for a user
    '''

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email,
        })


class  CustomDiscardAuthToken(APIView):
    '''
        this is a view to delete auth_token for a user 
    '''

    permission_classes = [IsAuthenticated]

    def post(self,request):
        request.user.auth_token.delete()

        return Response( status= status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    
    serializer_class = CustomTokenObtainPairSerializer
   

class ChangePasswordApiView(GenericAPIView):
 
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request):

        serializer = self.serializer_class(data= request.data , 
        context = {'request' : request})
        serializer.is_valid(raise_exception=True) 
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()

        return Response({'detail' : 'password updated'} , status= status.HTTP_200_OK)


class ProfileApiView(RetrieveUpdateAPIView):

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
            
            return Profile.objects.get(user= self.request.user)
    
    