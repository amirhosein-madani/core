import pytest
from django.shortcuts import reverse
from rest_framework.test import APIClient
from accounts.models import User
from django.utils import timezone
from ...models import Post


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def admin_user():
    user = User.objects.create_user(
        username="amir",
        password="amirmad2007",
        email="amirmadani901@gmail.com",
        phone_number="09912038679",
    )
    user.is_staff = True
    user.save()
    return user


@pytest.fixture
def another_admin():
    user = User.objects.create_user(
        username="mamad",
        password="amirmad2007",
        email="test@gmail.com",
        phone_number="09126809532",
    )
    user.is_staff = True
    user.save()
    return user


@pytest.fixture
def normal_user():
    user = User.objects.create_user(
        username="normal",
        password="amirmad2007",
        email="example@gmail.com",
        phone_number="09125179954",
    )
    return user


@pytest.fixture
def random_post(admin_user):
    post = Post.objects.create(
        author=admin_user.profile,
        title="test",
        status=True,
        content="this is test",
        published_date=timezone.now(),
    )
    return post


@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200_status(self, api_client):
        url = reverse("post-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self, api_client):
        url = reverse("post-list")

        data = {
            "title": "turk",
            "content": "turk lovers",
            "status": True,
            "published_date": timezone.now(),
        }

        response = api_client.post(url, data)

        assert response.status_code == 401

    def test_create_post_response_201_status(self, api_client, admin_user):
        url = reverse("post-list")
        api_client.force_authenticate(user=admin_user)

        data = {
            "title": "turk",
            "content": "turk lovers",
            "status": True,
            "published_date": timezone.now(),
        }

        response = api_client.post(url, data)
        assert response.status_code == 201
        assert Post.objects.filter(title=data["title"]).exists()

    def test_normal_user_create_post_response_403(self, api_client, normal_user):
        url = reverse("post-list")
        api_client.force_authenticate(user=normal_user)

        data = {
            "title": "turk",
            "content": "turk lovers",
            "status": True,
            "published_date": timezone.now(),
        }

        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_create_post_with_invalid_response_400_status(self, api_client, admin_user):
        url = reverse("post-list")
        api_client.force_authenticate(user=admin_user)

        data = {
            "title": "turk",
            "content": "turk lovers",
        }

        response = api_client.post(url, data)
        assert response.status_code == 400

    def test_post_detail_get_response_200_status(
        self, admin_user, random_post, api_client
    ):
        url = reverse("post-detail", kwargs={"pk": random_post.pk})
        response = api_client.get(url)
        assert response.status_code == 200

    def test_post_detail_update_response_200_status(
        self, admin_user, random_post, api_client
    ):
        api_client.force_authenticate(user=admin_user)
        url = reverse("post-detail", kwargs={"pk": random_post.pk})
        data = {
            "title": "test2",
            "status": False,
            "content": "this is test",
            "published_date": timezone.now(),
        }
        response = api_client.put(url, data)
        assert response.status_code == 200

    def test_post_detail_delete_response_200_status(
        self, admin_user, random_post, api_client
    ):
        api_client.force_authenticate(user=admin_user)
        url = reverse("post-detail", kwargs={"pk": random_post.pk})
        data = {
            "title": "test2",
            "status": False,
            "content": "this is test",
            "published_date": timezone.now(),
        }
        response = api_client.delete(url, data)
        assert response.status_code == 204

    def test_post_detail_update_response_400_status(
        self, admin_user, random_post, api_client
    ):
        api_client.force_authenticate(user=admin_user)
        url = reverse("post-detail", kwargs={"pk": random_post.pk})
        data = {
            "title": "test2",
        }
        response = api_client.put(url, data)
        assert response.status_code == 400

    def test_post_detail_update_response_401_status(self, random_post, api_client):
        url = reverse("post-detail", kwargs={"pk": random_post.pk})
        data = {
            "title": "test2",
        }
        response = api_client.put(url, data)
        assert response.status_code == 401

    def test_post_detail_another_user_get_post(
        self, random_post, another_admin, api_client
    ):

        api_client.force_authenticate(user=another_admin)
        url = reverse("post-detail", kwargs={"pk": random_post.pk})
        response = api_client.put(url)
        assert response.status_code == 403

    def test_post_detail_another_user_update_post(
        self, random_post, another_admin, api_client
    ):

        api_client.force_authenticate(user=another_admin)
        url = reverse("post-detail", kwargs={"pk": random_post.pk})
        data = {
            "title": "test2",
        }

        response = api_client.put(url, data)
        assert response.status_code == 403

    def test_post_detail_another_user_delete_post(
        self, random_post, another_admin, api_client
    ):

        api_client.force_authenticate(user=another_admin)
        url = reverse("post-detail", kwargs={"pk": random_post.pk})
        data = {
            "title": "test2",
        }

        response = api_client.delete(url, data)
        assert response.status_code == 403
