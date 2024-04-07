from django.test import SimpleTestCase
from django.urls import reverse, resolve

from login.views import login, callback, GetMyData


class TestUrls(SimpleTestCase):

    def test_login_url(self):
        url = reverse("login")
        self.assertEqual(resolve(url).func.view_class, login)

    def test_callback_url(self):
        url = reverse("callback")
        self.assertEqual(resolve(url).func.view_class, callback)

    def test_me_url(self):
        url = reverse("get_my_data")
        self.assertEqual(resolve(url).func.view_class, GetMyData)
