import pytest
from django.shortcuts import reverse
from rest_framework.test import APIClient
from accounts.models import User
from django.utils import timezone
from accounts.models import User
from ...models import Post
@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        username='amir',
        password='amirmad2007',
        email='amirmadani901@gmail.com',
        phone_number= '09912038679',
    )
    user.is_staff = True
    user.save()
    return user

@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200_status(self , api_client):
        url = reverse('post-list')
        response = api_client.get(url)
        assert response.status_code ==200

    def test_create_post_401_status(self , api_client):
        url = reverse('post-list')

        data = { 'title':"turk",
            'content':"turk lovers",
            'status':True,
            'published_date':timezone.now()}
        
        response =  api_client.post(url , data)
        
        assert response.status_code == 401

    def test_create_post_201_status(self , api_client , common_user):
        url = reverse('post-list')
        api_client.force_authenticate(user = common_user)

        data = { 'title':"turk",
            'content':"turk lovers",
            'status':True,
            'published_date':timezone.now()}

        response =  api_client.post(url , data)
        assert response.status_code == 201
        assert  Post.objects.filter(title= data['title']).exists()
        
    def test_create_post_with_invalid_400_status(self , api_client , common_user):
        url = reverse('post-list')
        api_client.force_authenticate(user = common_user)

        data = { 'title':"turk",
            'content':"turk lovers",
        }

        response =  api_client.post(url , data)
        assert response.status_code == 400
