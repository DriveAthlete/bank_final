import factory
from users.models import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: 'test_person{0}@t.ru'.format(n))
    money = 100.109
    currency = 1