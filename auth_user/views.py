from django.shortcuts import render
from django.contrib.auth.views import LogoutView, LoginView


# В'ю для логауту користувача
class UserLogoutView(LogoutView):
    next_page = "task-list"


# В'ю для логіну користувача
class UserLoginView(LoginView):
    template_name = "auth_user/login.html"


# В'ю для реєстрації користувача