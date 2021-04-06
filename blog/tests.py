from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from blog.views import index


# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_blog_view(self):
        found = resolve('/blog/')
        self.assertEqual(found.func, index)

    def test_blog_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        
        self.assertIn(b"Django TDD.", response.content)
        self.assertTrue(response.content.endswith(b'</html>'))


class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)
