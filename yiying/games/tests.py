from django.test import TestCase
from django.urls import resolve
from django.urls import reverse
from .views import index, detail

# Create your tests here.

class IndexTests(TestCase):

    def setUp(self):
        url = reverse('games:index')
        self.response = self.client.get(url)

    def test_index_view_status_code(self): 
        self.assertEquals(self.response.status_code, 200)

    def test_index_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, index)