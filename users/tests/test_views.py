from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from users.models import User
from rest_framework.authtoken.models import Token


class TestUserCreate(APITestCase):

    def setUp(self):
        self.url_create = reverse('user_create')
        self.client = APIClient()
        self.user = User.objects.create(email='1@t.ru', currency='1', money='9999999')

    def test_create_user_with_correct_data(self):
        data = {
            'email': '2@t.ru',
            'password': '12345',
            'currency': '1',
            'money': '10'
        }
        response = self.client.post(self.url_create, data, format='json')
        self.assertEquals(response.status_code, 201)
        test_user = User.objects.get(email='2@t.ru')
        self.assertEquals(test_user.currency, 1)
        self.assertEquals(test_user.money, 10.0)
        self.assertEquals(response.data, {'email': '2@t.ru', 'currency': 1, 'money': 10.0})

    def test_create_user_with_incorrect_data(self):
        data = {
            'email': 'asdasd',
            'password': '12345',
            'currency': '6',
            'money': 'asdasdasd'
        }
        response = self.client.post(self.url_create, data, format='json')
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data, {
            "email": ["Enter a valid email address."],
            "currency": ["\"6\" is not a valid choice."],
            "money": ["A valid number is required."]
        })

    def test_create_user_without_data(self):
        data = {}
        response = self.client.post(self.url_create, data, format='json')
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data, {
            "email": [
                "This field is required."
            ],
            "currency": [
                "This field is required."
            ],
            "money": [
                "This field is required."
            ],
            "password": [
                "This field is required."
            ]
        })


class TestInformView(APITestCase):

    def setUp(self):
        self.url_inform = reverse('user_inform')
        self.client = APIClient()
        self.user = User.objects.create(email='1@t.ru', currency='1', money='9999999', password='1')

    def test_without_auth(self):
        response = self.client.get(self.url_inform)
        self.assertEquals(response.status_code, 401)

    def test_with_auth(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_inform)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, {
            "user_inf": {
                "email": "1@t.ru",
                "currency": 1,
                "money": 9999999.0
            }
        })


class TestLoginView(APITestCase):

    def setUp(self):
        self.url_create = reverse('user_create')
        self.url_login = reverse('user_login')
        self.client = APIClient()
        self.data = {
            'email': '2@t.ru',
            'password': '12345',
            'currency': '1',
            'money': '10'
        }
        self.client.post(self.url_create, self.data, format='json')

    def test_with_correct_login_data(self):
        data = {
            'email': '2@t.ru',
            'password': '12345'
        }
        response = self.client.post(self.url_login, data, format='json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, {
            'token': f'%s' % str(Token.objects.get())
        })

    def test_with_incorrect_data(self):
        data = {
            'email': '6@t.ru',
            'password': '12345'
        }
        response = self.client.post(self.url_login, data, format='json')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {
            "error": "Invalid Credentials"
        })
