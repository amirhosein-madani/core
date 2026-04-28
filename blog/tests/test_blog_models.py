from django.test import TestCase
from django.utils import timezone
from ..models import Post
from accounts.models import User, Profile


class TestPost(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="ali_test",
            password="amirmad2007",
            email="alitest@gmail.com",
            phone_number="09125179954",
        )

    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            author=self.user.profile,
            title="turk",
            content="turk lovers",
            status=True,
            published_date=timezone.now(),
        )

        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertTrue(post.status)
