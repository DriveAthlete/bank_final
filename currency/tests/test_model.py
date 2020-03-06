from django.test import TestCase
from currency.models import Currency


class TestModels(TestCase):

    def setUp(self):
        self.cur = Currency.objects.create(currency=1, value=1.0)

    def test_str_method(self):
        self.assertEquals(str(self.cur), "1: 1.0")