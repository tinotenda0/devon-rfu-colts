from django.db import models
from enum import Enum
from django.contrib.auth.models import AbstractUser

# Match status differentiator

class MatchStatus(Enum):
    UPCOMING = "Upcoming"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    POSTPONED = "Postponed"

# Create your models here.

class  Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=100)
    privacy_consent = models.BooleanField()
    bio = models.TextField(max_length=1000)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    crest = models.TextField(max_length=1000)
    team_bio = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    venue = models.CharField(max_length=100)
    League = models.ForeignKey('League', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"
    
class Result(models.Model):
    result_id = models.AutoField(primary_key=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    home_tries = models.IntegerField()
    away_tries = models.IntegerField()
    notes = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.match}"

class Table(models.Model):
    table_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    league = models.ForeignKey('League', on_delete=models.CASCADE)
    played = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    points_for = models.IntegerField()
    points_against = models.IntegerField()
    point_difference = models.IntegerField()
    tries_for = models.IntegerField()
    tries_against = models.IntegerField()
    bonus_points = models.IntegerField()
    total_points = models.IntegerField()

    def __str__(self):
        return f"{self.team}"
    
class League(models.Model):
    league_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    season_year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    archived_status = models.BooleanField()
    notes = models.TextField(max_length=1000)

    def __str__(self):
        return self.name