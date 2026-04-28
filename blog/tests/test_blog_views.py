from django.test import TestCase, Client
from django.shortcuts import reverse
from django.utils import timezone
from ..models import Post
from accounts.models import User


class TestBlogView(TestCase):

    def setUp(self):

        self.client = Client()
        self.user = User.objects.create_user(
            username="ali_test",
            password="amirmad2007",
            email="alitest@gmail.com",
            phone_number="09125179954",
        )
        self.post = Post.objects.create(
            author=self.user.profile,
            title="turk",
            content="turk lovers",
            status=True,
            published_date=timezone.now(),
        )

    def test_blog_post_list_url_successful_200(self):
        url = reverse("post_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="post_list.html")

    def test_blog_index_url_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse("post_detail", kwargs={"slug": self.post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_index_url_anonymous_response(self):
        url = reverse("post_detail", kwargs={"slug": self.post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
