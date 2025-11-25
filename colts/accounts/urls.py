from django.urls import path
from .views import register, index, add_new, dashboard, club_admin_dash, new_team, edit_team, new_league, new_season, new_fixture, new_player
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
    path("edit_team/", edit_team, name="edit_team"),
    path("new_team/", new_team, name="new_team"),
    path("new_league/", new_league, name="new_league"),
    path("new_season/", new_season, name="new_season"),
    path("new_fixture/", new_fixture, name="new_fixture"),
    path("new_player/", new_player, name="new_player"),
]
