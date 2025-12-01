from . import views
from accounts.views import league_details as league_details
from accounts.views import team_details as team_details
from accounts.views import player_details as player_details
from accounts.views import match_details as match_details
from accounts.views import season_details as season_details
from accounts.views import archive as season_archive
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("table", views.table, name="table"),
    path("matches", views.matches, name="matches"),
    path("about", views.about, name="about"),
    path("auth", views.auth, name="auth"),
    path("contact", views.contact, name="contact"),
    path("leagues/<int:league_id>/", league_details, name="league_details"),
    path("teams/<int:team_id>/", team_details, name="team_details"),
    path("players/<int:player_id>/", player_details, name="player_details"),
    path("matches/<int:match_id>/", match_details, name="match_details"),
    path("seasons/<int:season_id>/", season_details, name="season_details"),
    path("seasons/archive/", season_archive, name="season_archive"),
]