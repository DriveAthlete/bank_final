from users.models import User

"""
Данный метод требуется для поиска пользователя по конкретному 
email
"""


def find_user(user_email):
    try:
        user = User.objects.get(email=user_email)
    except:
        return None

    return user
