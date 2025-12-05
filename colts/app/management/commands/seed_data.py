import random
import re
from datetime import date, time, timedelta

from django.core.management.base import BaseCommand
from django.db import transaction

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


TEAM_FILES = [
    "Barnstaple.png",
    "Bideford.png",
    "Brixham.png",
    "Collompton.png",
    "Crediton.png",
    "Dartmouth.png",
    "DevonportServices.png",
    "DevonYoungFarmers.png",
    "ExeterAthletic.png",
    "ExeterSaracens.png",
    "Exmouth.png",
    "Honiton.png",
    "Ilfracombe.png",
    "Ivybridge.png",
    "Kingsbridge.png",
    "NewCross.png",
    "NewtonAbbot.png",
    "NorthTawton.png",
    "OceanCity.png",
    "Okehampton.png",
    "OldPlymothian.png",
    "OldTechnicians.png",
    "Paignton.png",
    "PlymouthAlbion.png",
    "PlymouthArgaum.png",
    "PlymouthDolphins.png",
    "PlymstockOaks.png",
    "Salcombe.png",
    "Sidmouth.png",
    "SouthMolton.png",
    "Tavistock.png",
    "Teignmouth.png",
    "Tiverton.png",
    "Topsham.png",
    "TorbaySharks.png",
    "TorquayAthletic.png",
    "Torrington.png",
    "Totnes.png",
    "WescountryWasps.png",
    "Withycombe.png",
]


def humanise_team_name(filename: str) -> str:
    """Convert 'DevonYoungFarmers.png' -> 'Devon Young Farmers'."""
    base = filename.rsplit(".", 1)[0]
    # Insert space before capital letters (except first)
    name = re.sub(r"(?<!^)([A-Z])", r" \1", base)
    return name


RUGBY_POSITIONS = [
    "Prop",
    "Hooker",
    "Lock",
    "Flanker",
    "Number 8",
    "Scrum-half",
    "Fly-half",
    "Centre",
    "Wing",
    "Full-back",
]


class Command(BaseCommand):
    help = "Seeds the database with demo Devon RFU data"

    @transaction.atomic
    def handle(self, *args, **options):
        # Clear existing records for a clean seed (optional – comment out if you don't want this)
        self.stdout.write(self.style.WARNING("Deleting existing demo data..."))
        Result.objects.all().delete()
        Match.objects.all().delete()
        Standings.objects.all().delete()
        Player.objects.all().delete()
        LeagueMembership.objects.all().delete()
        League.objects.all().delete()
        Team.objects.all().delete()
        Season.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Existing data cleared."))

        # --- Season ---
        season = Season.objects.create(
            year="2024/2025",
            start_date=date(2024, 9, 1),
            end_date=date(2025, 5, 31),
            archived_status=False,
        )
        self.stdout.write(self.style.SUCCESS(f"Created Season: {season.year}"))

        # --- Leagues ---
        # You can rename these to match your actual structure
        league_north = League.objects.create(
            name="Devon Colts North",
            age_group="U18",
            gender="Male",
            season=season,
            notes="Demo league for northern clubs.",
        )
        league_south = League.objects.create(
            name="Devon Colts South",
            age_group="U18",
            gender="Male",
            season=season,
            notes="Demo league for southern clubs.",
        )
        self.stdout.write(self.style.SUCCESS("Created 2 leagues: North & South"))

        # --- Teams ---
        teams = []
        for filename in TEAM_FILES:
            team_name = humanise_team_name(filename)
            team = Team.objects.create(
                name=team_name,
                crest=f"crests/{filename}",
                team_bio=f"{team_name} Colts side for the 2024/25 season.",
                gender="Male",
                age_group="U18",
            )
            teams.append(team)
        self.stdout.write(
            self.style.SUCCESS(f"Created {len(teams)} teams from crest files.")
        )

        # Split teams between two leagues
        half = len(teams) // 2
        north_teams = teams[:half]
        south_teams = teams[half:]

        # --- League Memberships ---
        memberships = []
        for team in north_teams:
            memberships.append(
                LeagueMembership(
                    league=league_north,
                    team=team,
                    season=season,
                )
            )
        for team in south_teams:
            memberships.append(
                LeagueMembership(
                    league=league_south,
                    team=team,
                    season=season,
                )
            )
        LeagueMembership.objects.bulk_create(memberships)
        self.stdout.write(
            self.style.SUCCESS(
                f"Created {len(memberships)} league memberships for {season.year}."
            )
        )

        # --- Players ---
        self.stdout.write("Creating demo players...")
        players_to_create = []
        for team in teams:
            for i in range(1, 6):  # 5 players per team
                position = RUGBY_POSITIONS[(i - 1) % len(RUGBY_POSITIONS)]
                age = random.randint(16, 18)
                players_to_create.append(
                    Player(
                        name=f"{team.name} Player {i}",
                        age=age,
                        position=position,
                        privacy_consent=True if i != 5 else False,  # last one: no consent
                        bio=f"Demo player {i} for {team.name}, plays as {position}.",
                        team=team,
                    )
                )
        Player.objects.bulk_create(players_to_create)
        self.stdout.write(
            self.style.SUCCESS(
                f"Created {len(players_to_create)} players (5 per team)."
            )
        )

        # --- Matches + Results ---
        # Simple pairing: each league gets a small set of fixtures
        self.stdout.write("Creating demo matches and results...")

        def create_league_fixtures(league, league_teams, start_offset_weeks=0):
            matches_created = []
            results_created = []

            match_date = season.start_date + timedelta(weeks=start_offset_weeks)
            match_time = time(14, 0)  # 2pm KO

            # Pair teams in order: (0 vs 1), (2 vs 3), etc.
            for round_no in range(3):  # 3 rounds
                round_date = match_date + timedelta(weeks=round_no)
                for i in range(0, len(league_teams) - 1, 2):
                    home_team = league_teams[i]
                    away_team = league_teams[i + 1]

                    match = Match.objects.create(
                        league=league,
                        season=season,
                        date=round_date,
                        time=match_time,
                        venue=f"{home_team.name} RFC",
                        home_team=home_team,
                        away_team=away_team,
                    )
                    matches_created.append(match)

                    # Simple random-ish scoreline
                    home_tries = random.randint(1, 6)
                    away_tries = random.randint(0, 5)
                    home_score = home_tries * 5 + random.choice([0, 2, 3, 5])
                    away_score = away_tries * 5 + random.choice([0, 2, 3, 5])

                    result = Result(
                        match=match,
                        home_score=home_score,
                        away_score=away_score,
                        home_tries=home_tries,
                        away_tries=away_tries,
                        notes="Demo result auto-generated for testing.",
                    )
                    results_created.append(result)

            Result.objects.bulk_create(results_created)
            return matches_created, results_created

        north_matches, north_results = create_league_fixtures(
            league_north, north_teams, start_offset_weeks=0
        )
        south_matches, south_results = create_league_fixtures(
            league_south, south_teams, start_offset_weeks=1
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Created {len(north_matches) + len(south_matches)} matches and "
                f"{len(north_results) + len(south_results)} results."
            )
        )

        # --- Standings ---
        self.stdout.write("Creating demo standings...")

        def create_standings_for_league(league, league_teams):
            standings_to_create = []
            for idx, team in enumerate(league_teams):
                # Fake some semi-realistic stats
                played = random.randint(3, 9)
                wins = random.randint(0, played)
                losses = random.randint(0, played - wins)
                draws = played - wins - losses

                points_for = random.randint(50, 250)
                points_against = random.randint(40, 230)
                point_diff = points_for - points_against

                tries_for = random.randint(10, 40)
                tries_against = random.randint(8, 35)

                bonus_points = random.randint(0, 5)
                total_points = wins * 4 + draws * 2 + bonus_points

                standings_to_create.append(
                    Standings(
                        league=league,
                        season=season,
                        team=team,
                        played=played,
                        wins=wins,
                        draws=draws,
                        losses=losses,
                        points_for=points_for,
                        points_against=points_against,
                        point_difference=point_diff,
                        tries_for=tries_for,
                        tries_against=tries_against,
                        bonus_points=bonus_points,
                        total_points=total_points,
                    )
                )
            Standings.objects.bulk_create(standings_to_create)
            return standings_to_create

        north_standings = create_standings_for_league(league_north, north_teams)
        south_standings = create_standings_for_league(league_south, south_teams)

        self.stdout.write(
            self.style.SUCCESS(
                f"Created {len(north_standings) + len(south_standings)} standings rows."
            )
        )

        self.stdout.write(self.style.SUCCESS("✅ Demo data seeding complete."))
