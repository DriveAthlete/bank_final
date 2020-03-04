from django.test import TestCase
from users.models import User
from users.tests.user_factory import UserFactory


class UserModelTest(TestCase):


    def test_email_field_label(self):
        user = UserFactory.create()
        field_label = user.__meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'Email')

    def test_email_max_length(self):
        user = UserFactory.create()
        field_label = user.__meta.get_field('email').max_lenght
        self.assertEquals(field_label, '255')

    def test_currency_field_label(self):
        user = UserFactory.create()
        field_label = user.__meta.get_field('currency').verbose_name
        self.assertEquals(field_label, 'Currency')

    def test_money_field_label(self):
        user = UserFactory.create()
        field_label = user.__meta.get_field('money').verbose_name
        self.assertEquals(field_label, 'Money')

    def test_object_name_is_email(self):
        user = UserFactory.create()
        expected_object_name = user.email
        self.assertEquals(expected_object_name, str(user))
