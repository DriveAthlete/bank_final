from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from users.models import User
from currency.models import Currency
from transfer.models import Transfer
import json


class TestViews(APITestCase):

    def setUp(self):
        User.objects.create(email='1@t.ru', currency='1', money='9999999')
        User.objects.create(email='2@t.ru', currency='2', money='9999999')
        Currency.objects.create(currency=1, value='0.9')
        Currency.objects.create(currency=2, value='1')

        self.client = APIClient()
        self.list_url = reverse('transfer_list')
        self.create_url = reverse('transfer_create')

    def test_transfer_list_GET(self):
        user = User.objects.get(email='1@t.ru')

        self.client.force_authenticate(user=user)
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_transfer_list_GET_user_is_not_auth(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 401)

    def test_transfer_create_POST_with_correct_data(self):
        user = User.objects.get(email='1@t.ru')
        self.client.force_authenticate(user=user)
        data = {
            'to_user': '2@t.ru',
            'amount': '100'
        }
        responce = self.client.post(self.create_url, data=data, format='json')
        self.assertEquals(responce.status_code, 201)
        self.assertEquals(Transfer.objects.count(), 1)
        self.assertEquals(str(Transfer.objects.get().to_user), '2@t.ru')
        self.assertEquals(str(Transfer.objects.get().from_user), '1@t.ru')

    def test_transfer_create_POST_with_incorrect_user_email(self):
        user = User.objects.get(email='1@t.ru')
        self.client.force_authenticate(user=user)
        data = {
            'to_user': 'addasdasd',
            'amount': '100'
        }
        responce = self.client.post(self.create_url, data=data, format='json')
        self.assertEquals(responce.status_code, 400)
        self.assertEquals(Transfer.objects.count(), 0)

    def test_transfer_create_POST_with_incorrect_amount(self):
        user = User.objects.get(email='1@t.ru')
        self.client.force_authenticate(user=user)
        data = {
            'to_user': '2@t.ru',
            'amount': 'asdasdasd'
        }
        responce = self.client.post(self.create_url, data=data, format='json')
        self.assertEquals(responce.status_code, 400)
        self.assertEquals(Transfer.objects.count(), 0)

    def test_transfer_create_POST_without_data(self):
        user = User.objects.get(email='1@t.ru')
        self.client.force_authenticate(user=user)
        data = {}
        responce = self.client.post(self.create_url, data=data, format='json')
        self.assertEquals(responce.status_code, 400)
        self.assertEquals(Transfer.objects.count(), 0)
