from django.test import TestCase
from users.models import User



# class UserModelTest(TestCase):
#
#     def setUp(self):
#         User.objects.create(email='12@t.ru', currency='1', money='101010')
#
#     def test_email_field_label(self):
#         user = User.objects.get(pk=1)
#         field_label = user.__meta.get_field('email').verbose_name
#         self.assertEquals(field_label, 'Email')
#
#     def test_email_max_length(self):
#         user = User.objects.get(pk=1)
#         field_label = user.__meta.get_field('email').max_lenght
#         self.assertEquals(field_label, '255')
#
#     def test_currency_field_label(self):
#         user = User.objects.get(pk=1)
#         field_label = user.__meta.get_field('currency').verbose_name
#         self.assertEquals(field_label, 'Currency')
#
#     def test_money_field_label(self):
#         user = User.objects.get(pk=1)
#         field_label = user.__meta.get_field('money').verbose_name
#         self.assertEquals(field_label, 'Money')
#
#     def test_object_name_is_email(self):
#         user = User.objects.get(pk=1)
#         expected_object_name = user.email
#         self.assertEquals(expected_object_name, str(user))
