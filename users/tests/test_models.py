from django.test import TestCase
from users.models import User


class TestModelUser(TestCase):

    def setUp(self):
        self.user = User.objects.create(email='1@t.ru', currency='1', money='9999999')

    def test_str_method(self):
        self.assertEquals(str(self.user), '1@t.ru')

