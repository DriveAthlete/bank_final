from django.urls import path
from users.views import *

urlpatterns = [
    path('', UserCreateView.as_view(), name="user_create"),
    path('login/', LoginView.as_view(), name="login"),
    path('inform/', UserInformView.as_view()),
]
