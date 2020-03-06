from django.test import SimpleTestCase
from django.urls import resolve, reverse

from users.views import UserCreateView, UserInformView, LoginView


class TestUrlsUser(SimpleTestCase):

    def setUp(self):
        self.url_create = reverse('user_create')
        self.url_login = reverse('user_login')
        self.url_inform = reverse('user_inform')

    def test_url_create(self):
        self.assertEquals(resolve(self.url_create).func.view_class, UserCreateView)

    def test_url_login(self):
        self.assertEquals(resolve(self.url_login).func.view_class, LoginView)

    def test_url_inform(self):
        self.assertEquals(resolve(self.url_inform).func.view_class, UserInformView)


