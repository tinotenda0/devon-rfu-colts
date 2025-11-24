from django.db import models

# Create your models here.

class Season(models.Model):
    year = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    archived_status = models.BooleanField(default=False)

    def __str__(self):
        return self.year

class League(models.Model):
    name = models.CharField(max_length=100)          
    age_group = models.CharField(max_length=20)      
    gender = models.CharField(max_length=10)        
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='leagues')
    notes = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.name} ({self.age_group}, {self.gender}, {self.season})"

class Team(models.Model):
    name = models.CharField(max_length=100)
    crest = models.TextField(max_length=1000, blank=True)
    team_bio = models.TextField(max_length=1000, blank=True)
    gender = models.CharField(max_length=10)        
    age_group = models.CharField(max_length=20)      

    def __str__(self):
        return f"{self.name} ({self.age_group}, {self.gender})"
    
class LeagueMembership(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=100)
    privacy_consent = models.BooleanField()
    bio = models.TextField(max_length=1000, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=100)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')

class Result(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE)
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    home_tries = models.IntegerField()
    away_tries = models.IntegerField()
    notes = models.TextField(max_length=1000, blank=True)

class Standings(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    points_for = models.IntegerField(default=0)
    points_against = models.IntegerField(default=0)
    point_difference = models.IntegerField(default=0)
    tries_for = models.IntegerField(default=0)
    tries_against = models.IntegerField(default=0)
    bonus_points = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
