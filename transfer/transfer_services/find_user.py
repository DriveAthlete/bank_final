from users.models import User


def find_user(user_email):
    user = User.objects.get(email=user_email)
    if user is None:
        return None
    return user
