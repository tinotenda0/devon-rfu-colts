from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('table', views.table, name='table'),

    path('matches', views.matches, name='matches'),

    path('about', views.about, name='about'),
]