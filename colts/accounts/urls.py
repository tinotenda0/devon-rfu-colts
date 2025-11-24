from django.urls import path
from .views import register, index, add_new, dashboard, club_admin_dash
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", index, name="index"),
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("add_new/", add_new, name="add_new"),
    path("dashboard/", dashboard, name="dashboard"),
    path("dash/", club_admin_dash, name="club_admin_dash"),
]
