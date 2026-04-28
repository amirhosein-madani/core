from django.test import TestCase
from ..forms import PostFOrm
from datetime import datetime


class TestPostForm(TestCase):

    def test_post_form_with_valid_data(self):
        form = PostFOrm(
            data={
                "title": "amir",
                "content": "this is a test",
                "status": True,
                "published_date": datetime.now(),
            }
        )

        self.assertTrue(form.is_valid())

    def test_post_form_with_invalid_data(self):

        form = PostFOrm()
        self.assertFalse(form.is_valid())
