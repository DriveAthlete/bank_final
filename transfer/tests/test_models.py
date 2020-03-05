from django.test import TestCase
from transfer.models import Transfer
from users.models import User


class TestModel(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(email='1@t.ru', currency='1', money='9999999')
        self.user2 = User.objects.create(email='2@t.ru', currency='2', money='9999999')
        self.amount = 1.1
        self.transfer = Transfer.objects.create(from_user=self.user1, to_user=self.user2, amount=self.amount)

    def test_save_model(self):
        self.assertEquals(str(self.transfer), '1@t.ru sent 1.1 to 2@t.ru')
