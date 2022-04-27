from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register_request, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("ques2", views.ques2, name="ques2"),
    path("ques3", views.ques3, name="ques3"),
    path("result", views.result, name="result"),
]
