import datetime
from django.core.management.base import BaseCommand
from app.models import (
    Season,
    League,
    Team,
    LeagueMembership,
    Player,
    Match,
    Result,
    Standings,
)


class Command(BaseCommand):
    help = "Seeds the database with initial data for all models except users."

    def handle(self, *args, **options):
        self.stdout.write("Starting database seeding...")

        # Clean up old data to prevent duplicates
        self.stdout.write("Clearing old data...")
        Standings.objects.all().delete()
        Result.objects.all().delete()
        Match.objects.all().delete()
        Player.objects.all().delete()
        LeagueMembership.objects.all().delete()
        League.objects.all().delete()
        Team.objects.all().delete()
        Season.objects.all().delete()

        # --- 1. Create Seasons ---
        self.stdout.write("Creating Seasons...")
        season1, _ = Season.objects.get_or_create(
            year="2023-2024",
            defaults={
                "start_date": datetime.date(2023, 9, 1),
                "end_date": datetime.date(2024, 5, 31),
            },
        )
        season2, _ = Season.objects.get_or_create(
            year="2024-2025",
            defaults={
                "start_date": datetime.date(2024, 9, 1),
                "end_date": datetime.date(2025, 5, 31),
            },
        )
        season3, _ = Season.objects.get_or_create(
            year="2025-2026",
            defaults={
                "start_date": datetime.date(2025, 9, 1),
                "end_date": datetime.date(2026, 5, 31),
            },
        )

        # --- 2. Create Teams ---
        self.stdout.write("Creating Teams...")
        team1, _ = Team.objects.get_or_create(name="Exeter Chiefs Colts", gender="Male", age_group="U18")
        team2, _ = Team.objects.get_or_create(name="Plymouth Albion Colts", gender="Male", age_group="U18")
        team3, _ = Team.objects.get_or_create(name="Barnstaple RFC Colts", gender="Male", age_group="U18")
        team4, _ = Team.objects.get_or_create(name="Topsham Girls", gender="Female", age_group="U16")
        team5, _ = Team.objects.get_or_create(name="Ivybridge Girls", gender="Female", age_group="U16")
        team6, _ = Team.objects.get_or_create(name="Crediton Girls", gender="Female", age_group="U16")

        # --- 3. Create Leagues ---
        self.stdout.write("Creating Leagues...")
        league1, _ = League.objects.get_or_create(name="Devon Merit Table 1", age_group="U18", gender="Male", season=season2)
        league2, _ = League.objects.get_or_create(name="Devon Girls League A", age_group="U16", gender="Female", season=season2)
        league3, _ = League.objects.get_or_create(name="Devon Merit Table 2", age_group="U18", gender="Male", season=season2)

        # --- 4. Create League Memberships ---
        self.stdout.write("Creating League Memberships...")
        LeagueMembership.objects.get_or_create(league=league1, team=team1, season=season2)
        LeagueMembership.objects.get_or_create(league=league1, team=team2, season=season2)
        LeagueMembership.objects.get_or_create(league=league1, team=team3, season=season2)
        LeagueMembership.objects.get_or_create(league=league2, team=team4, season=season2)
        LeagueMembership.objects.get_or_create(league=league2, team=team5, season=season2)
        LeagueMembership.objects.get_or_create(league=league2, team=team6, season=season2)

        # --- 5. Create Players ---
        self.stdout.write("Creating Players...")
        Player.objects.get_or_create(name="John Smith", age=17, position="Fly-half", privacy_consent=True, team=team1)
        Player.objects.get_or_create(name="Peter Jones", age=18, position="Prop", privacy_consent=True, team=team1)
        Player.objects.get_or_create(name="David Williams", age=17, position="Full-back", privacy_consent=False, team=team2)
        Player.objects.get_or_create(name="Emily White", age=15, position="Winger", privacy_consent=True, team=team4)
        Player.objects.get_or_create(name="Sarah Brown", age=16, position="Scrum-half", privacy_consent=True, team=team4)
        Player.objects.get_or_create(name="Jessica Green", age=15, position="Center", privacy_consent=True, team=team5)

        # --- 6. Create Matches ---
        self.stdout.write("Creating Matches...")
        match1, _ = Match.objects.get_or_create(
            league=league1, season=season2, date=datetime.date(2024, 10, 5), time=datetime.time(14, 30),
            venue="Exeter RFC", home_team=team1, away_team=team2
        )
        match2, _ = Match.objects.get_or_create(
            league=league1, season=season2, date=datetime.date(2024, 10, 12), time=datetime.time(15, 0),
            venue="Barnstaple RFC", home_team=team3, away_team=team1
        )
        match3, _ = Match.objects.get_or_create(
            league=league2, season=season2, date=datetime.date(2024, 10, 19), time=datetime.time(13, 0),
            venue="Topsham RFC", home_team=team4, away_team=team5
        )

        # --- 7. Create Results ---
        self.stdout.write("Creating Results...")
        Result.objects.get_or_create(
            match=match1, defaults={'home_score': 25, 'away_score': 15, 'home_tries': 4, 'away_tries': 2}
        )
        Result.objects.get_or_create(
            match=match2, defaults={'home_score': 10, 'away_score': 30, 'home_tries': 1, 'away_tries': 5}
        )
        Result.objects.get_or_create(
            match=match3, defaults={'home_score': 22, 'away_score': 22, 'home_tries': 3, 'away_tries': 3}
        )

        # --- 8. Create Standings ---
        self.stdout.write("Creating Standings...")
        # For league 1
        Standings.objects.get_or_create(
            league=league1, season=season2, team=team1, defaults={
                'played': 2, 'wins': 1, 'losses': 1, 'total_points': 6
            }
        )
        Standings.objects.get_or_create(
            league=league1, season=season2, team=team2, defaults={
                'played': 1, 'wins': 0, 'losses': 1, 'total_points': 1
            }
        )
        Standings.objects.get_or_create(
            league=league1, season=season2, team=team3, defaults={
                'played': 1, 'wins': 1, 'losses': 0, 'total_points': 5
            }
        )
        # For league 2
        Standings.objects.get_or_create(
            league=league2, season=season2, team=team4, defaults={
                'played': 1, 'wins': 0, 'draws': 1, 'losses': 0, 'total_points': 2
            }
        )
        Standings.objects.get_or_create(
            league=league2, season=season2, team=team5, defaults={
                'played': 1, 'wins': 0, 'draws': 1, 'losses': 0, 'total_points': 2
            }
        )

        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully!"))