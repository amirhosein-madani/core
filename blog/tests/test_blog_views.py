from django.test import TestCase , SimpleTestCase
from django.urls import reverse , resolve
from . views import IndesxVIew , PostListView , MaktabView , PostDetailView
# Create your tests here.

class TestUrl(SimpleTestCase):

    def test_blog_post_detail_url_resovle(self):
        url = reverse('post_detail' , kwargs= {'slug' : 'kos'})
        self.assertEqual(resolve(url).func.view_class , PostDetailView)

    def test_blog_post_list_url_resovle(self):
        url = reverse('post_list')
        self.assertEqual(resolve(url).func.view_class , PostListView)

    def test_blog_index_url_resovle(self):
        url = reverse('index')
        self.assertAlmostEqual(resolve(url).func.view_class , IndesxVIew)
        