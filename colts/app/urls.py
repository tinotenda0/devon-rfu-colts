from . import views

from django.urls import path
from .views import (
    season_list,
    season_add,
    season_edit,
    season_delete,
    season_archive,
    season_unarchive,
)

urlpatterns = [
    path("seasons/", season_list, name="season_list"),
    path("seasons/add/", season_add, name="season_add"),
    path("seasons/<int:season_id>/edit/", season_edit, name="season_edit"),
    path("seasons/<int:season_id>/delete/", season_delete, name="season_delete"),
    path("seasons/<int:season_id>/archive/", season_archive, name="season_archive"),
    path(
        "seasons/<int:season_id>/unarchive/", season_unarchive, name="season_unarchive"
    ),
]

urlpatterns = [
    path("", views.index, name="index"),
    path("table", views.table, name="table"),
    path("matches", views.matches, name="matches"),
    path("about", views.about, name="about"),
    path("auth", views.auth, name="auth"),
]
