from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import CustomUserRegistrationForm, ClubAdminCreationForm, AddTeamForm, AddLeagueForm, AddSeasonForm, AddFixtureForm, AddPlayerForm, AddResultForm
from django.contrib.auth import login
from accounts.decorators import admin_required, club_admin_required
from app.models import Season, League, Team, Match, Result, Player
from accounts.models import CustomUser

def teams(request):
    try:
        teams = Team.objects.all()
    except Exception as e:
        print(f"Error fetching teams: {e}")
        teams = []
    return teams

def users(request):
    try:
        users = CustomUser.objects.all()
    except Exception as e:
        print(f"Error fetching users: {e}")
        users = []
    return users

@admin_required
def index(request):
    club_admins = CustomUser.objects.filter(role="club_admin")
    context = {
        "seasons": Season.objects.all().order_by("-start_date"),
        "leagues": League.objects.all(),
        "teams": Team.objects.all(),
        "club_admins": club_admins,
        "matches": Match.objects.all().order_by("-date")[:10],
    }

    # if request.user.is_authenticated:
    #     if request.user.is_superuser or request.user.role == "admin":
    #         return redirect("admin_dashboard")
    #     elif request.user.role == "club_admin":
    #         return redirect("club_admin_dash")
    return render(request, "accounts/index.html", context)


def register(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect("index")
    else:
        form = CustomUserRegistrationForm()
    return render(request, "registration/register.html", {"form": form})

@admin_required
def add_new(request):
    clubs = teams(request)
    if request.method == "POST":
        form = ClubAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ClubAdminCreationForm()
    return render(request, "accounts/add_new.html", {"form": form, "clubs": clubs})

@admin_required
def edit_user(request, user_id):
    user_profile = get_object_or_404(CustomUser, pk=user_id)
    if request.method == "POST":
        form = ClubAdminCreationForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ClubAdminCreationForm(instance=user_profile)
    return render(request, "accounts/edit_user.html", {"form": form, "user_profile": user_profile})


@admin_required
def delete_user(request, user_id):
    user_profile = get_object_or_404(CustomUser, pk=user_id)
    if request.method == "POST":
        user_profile.delete()
        return redirect("dashboard")
    return render(request, "accounts/delete_user.html", {"user_profile": user_profile})

@club_admin_required
def club_admin_dash(request):
    team = request.user.club
    if request.method == 'POST':
        form = AddTeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect('club_admin_dash')
    else:
        form = AddTeamForm(instance=team)

    players = Player.objects.filter(team=team)
    home_matches = Match.objects.filter(home_team=team).order_by("-date")
    away_matches = Match.objects.filter(away_team=team).order_by("-date")
    matches = (home_matches | away_matches).distinct().order_by("-date")[:10]

    context = {
        "club": team,
        "players": players,
        "matches": matches,
        "form": form,
    }
    return render(request, "accounts/club_admin_dash.html", context)

@admin_required
def new_team(request):
    if request.method == "POST":
        form = AddTeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AddTeamForm()
    return render(request, "teams/new_team.html", {"form": form})

@club_admin_required
def new_league(request):
    if request.method == "POST":
        form = AddLeagueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AddLeagueForm()
    return render(request, "leagues/new_league.html", {"form": form})

@admin_required
def new_season(request):
    if request.method == "POST":
        form = AddSeasonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AddSeasonForm()
    return render(request, "seasons/new_season.html", {"form": form})

@admin_required
def manage_seasons(request):
    seasons = Season.objects.all()
    return render(request, "seasons/manage_seasons.html", {"seasons": seasons})

@admin_required
def edit_season(request, season_id):
    season = get_object_or_404(Season, pk=season_id)
    if request.method == "POST":
        form = AddSeasonForm(request.POST, instance=season)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AddSeasonForm(instance=season)
    return render(request, "seasons/new_season.html", {"form": form, "season": season})

@admin_required
def delete_season(request, season_id):
    season = get_object_or_404(Season, pk=season_id)
    if request.method == "POST":
        season.delete()
        return redirect("index")
    return render(request, "seasons/delete_season.html", {"season": season})

@admin_required
def archive_season(request, season_id):
    season = get_object_or_404(Season, pk=season_id)
    if request.method == "POST":
        season.archived_status = not season.archived_status
        season.save()
        return redirect("manage_seasons")
    return render(request, "seasons/archive_season.html", {"season": season})


@club_admin_required
def new_fixture(request):
    team = request.user.club
    if not team:
        return redirect('club_admin_dash')
    if request.method == "POST":
        form = AddFixtureForm(request.POST)
        if form.is_valid():
            fixture = form.save(commit=False)
            fixture.home_team = team
            fixture.save()
            return redirect("club_admin_dash")
    else:
        form = AddFixtureForm(initial={'home_team': team})
    return render(request, "matches/new_fixture.html", {"form": form})

@club_admin_required
def new_result(request, team_id=None):
    team = request.user.club
    if not team:
        return redirect('club_admin_dash')

    if team_id:
        # If team_id is provided, it means we are adding a result for a specific match
        # where the current user's team is either home or away.
        # The form should be pre-filled with this match.
        match = get_object_or_404(Match, pk=team_id)
        if request.method == "POST":
            form = AddResultForm(team=team, data=request.POST)
            if form.is_valid():
                result = form.save(commit=False)
                result.match = match
                result.save()
                return redirect("club_admin_dash")
        else:
            form = AddResultForm(team=team, initial={'match': match})
    else:
        if request.method == "POST":
            form = AddResultForm(team=team, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect("club_admin_dash")
        else:
            form = AddResultForm(team=team)
    return render(request, "matches/new_result.html", {"form": form})

@club_admin_required
def edit_match(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    if request.method == "POST":
        form = AddFixtureForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect("club_admin_dash")
    else:
        form = AddFixtureForm(instance=match)
    return render(request, "matches/new_fixture.html", {"form": form, "match": match})

@club_admin_required
def edit_result(request, result_id):
    result = get_object_or_404(Result, pk=result_id)
    if request.method == "POST":
        form = AddResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect("club_admin_dash")
    else:
        form = AddResultForm(instance=result)
    return render(request, "matches/new_result.html", {"form": form, "result": result})


@club_admin_required
def delete_match(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    if request.method == "POST":
        match.delete()
        return redirect("club_admin_dash")
    return render(request, "matches/delete_match.html", {"match": match})

@club_admin_required
def new_player(request):
    if request.method == "POST":
        form = AddPlayerForm(request.POST, user=request.user)
        if form.is_valid():
            player = form.save(commit=False)
            player.team = request.user.club
            player.save()
            return redirect("club_admin_dash")
    else:
        form = AddPlayerForm(user=request.user)
    return render(request, "players/new_player.html", {"form": form})

@admin_required
def manage_leagues(request):
    leagues = League.objects.all()
    return render(request, "leagues/manage_leagues.html", {"leagues": leagues})

@admin_required
def edit_league(request, league_id):
    league = get_object_or_404(League, pk=league_id)
    if request.method == "POST":
        form = AddLeagueForm(request.POST, instance=league)
        if form.is_valid():
            form.save()
            return redirect("manage_leagues")
    else:
        form = AddLeagueForm(instance=league)
    return render(request, "leagues/new_league.html", {"form": form, "league": league})

@club_admin_required
def edit_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == "POST":
        form = AddTeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect("manage_teams")
    else:
        form = AddTeamForm(instance=team)
    return render(request, "teams/new_team.html", {"form": form, "team": team})

@admin_required
def delete_league(request, league_id):
    league = get_object_or_404(League, pk=league_id)
    if request.method == "POST":
        league.delete()
        return redirect("manage_leagues")
    return render(request, "leagues/delete_league.html", {"league": league})
@admin_required
def manage_teams(request):
    teams = Team.objects.all()
    return render(request, "teams/manage_teams.html", {"teams": teams})

@admin_required
def delete_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == "POST":
        team.delete()
        return redirect("manage_teams")
    return render(request, "teams/delete_team.html", {"team": team})

@admin_required
def manage_players(request):
    team = request.user.club
    players = Player.objects.filter(team=team)
    return render(request, "players/manage_players.html", {"players": players, "club": team})

@club_admin_required
def edit_player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    if request.method == "POST":
        form = AddPlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect("manage_players")
    else:
        form = AddPlayerForm(instance=player)
    return render(request, "players/new_player.html", {"form": form, "player": player})

@club_admin_required
def delete_player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    if request.method == "POST":
        player.delete()
        return redirect("manage_players")
    return render(request, "players/delete_player.html", {"player": player})

#automatic standings per league
def calculate_standings(league):
    teams = Team.objects.filter(leaguemembership__league=league)
    standings = {}

    for team in teams:
        standings[team] = {
            'played': 0,
            'wins': 0,
            'draws': 0,
            'losses': 0,
            'points_for': 0,
            'points_against': 0,
            'point_difference': 0,
            'tries_for': 0,
            'tries_against': 0,
            'bonus_points': 0,
            'total_points': 0,
        }

    matches = Match.objects.filter(league=league)

    for match in matches:
        home_team = match.home_team
        away_team = match.away_team
        result = Result.objects.filter(match=match).first()

        if result:
            # Update played count
            standings[home_team]['played'] += 1
            standings[away_team]['played'] += 1

            # Update points for/against
            standings[home_team]['points_for'] += result.home_score
            standings[home_team]['points_against'] += result.away_score
            standings[away_team]['points_for'] += result.away_score
            standings[away_team]['points_against'] += result.home_score

            # Update tries for/against
            standings[home_team]['tries_for'] += result.home_tries
            standings[home_team]['tries_against'] += result.away_tries
            standings[away_team]['tries_for'] += result.away_tries
            standings[away_team]['tries_against'] += result.home_tries

            # Determine win/loss/draw and allocate points
            if result.home_score > result.away_score:
                standings[home_team]['wins'] += 1
                standings[home_team]['total_points'] += 4  # Win points
                standings[away_team]['losses'] += 1
            elif result.away_score> result.home_score:
                standings[away_team]['wins'] += 1
                standings[away_team]['total_points'] += 4  # Win points
                standings[home_team]['losses'] += 1
            else:
                standings[home_team]['draws'] += 1
                standings[home_team]['total_points'] += 2  # Draw points
                standings[away_team]['draws'] += 1
                standings[away_team]['total_points'] += 2  # Draw points

            # Bonus points (example: try bonus, losing bonus)
            if result.home_tries >= 4:
                standings[home_team]['bonus_points'] += 1
                standings[home_team]['total_points'] += 1
            if result.away_score >= result.home_score - 7 and result.away_score < result.home_score:
                standings[away_team]['bonus_points'] += 1
                standings[away_team]['total_points'] += 1

            if result.away_tries >= 4:
                standings[away_team]['bonus_points'] += 1
                standings[away_team]['total_points'] += 1
            if result.home_score >= result.away_score - 7 and result.home_score < result.away_score:
                standings[home_team]['bonus_points'] += 1
                standings[home_team]['total_points'] += 1

    # Calculate point difference
    for team_standing in standings.values():
        team_standing['point_difference'] = team_standing['points_for'] - team_standing['points_against']

    # Convert to a list of dictionaries for easier sorting and template rendering
    standings_list = []
    for team, data in standings.items():
        standings_list.append({
            'team': team,
            'played': data['played'],
            'wins': data['wins'],
            'draws': data['draws'],
            'losses': data['losses'],
            'points_for': data['points_for'],
            'points_against': data['points_against'],
            'point_difference': data['point_difference'],
            'tries_for': data['tries_for'],
            'tries_against': data['tries_against'],
            'bonus_points': data['bonus_points'],
            'total_points': data['total_points'],
        })

    # Sort standings: total points, then point difference, then points for
    standings_list.sort(key=lambda x: (x['total_points'], x['point_difference'], x['points_for']), reverse=True)

    return standings_list

# Detailed frontend league view with teams, matches, players and all stats
def league_details(request, league_id):
    league = get_object_or_404(League, pk=league_id)
    teams_in_league = Team.objects.filter(leaguemembership__league=league)
    fixtures = Match.objects.filter(league=league, date__gte=timezone.now()).order_by('date')
    recent_matches = Result.objects.filter(match__league=league).order_by('-match__date')[:5]

    standings = calculate_standings(league)

    context = {
        'league': league,
        'teams_in_league': teams_in_league,
        'fixtures': fixtures,
        'recent_matches': recent_matches,
        'standings': standings,
        "all_leagues": League.objects.all(),
        "all_seasons": Season.objects.all(),
    }
    return render(request, 'leagues/league_details.html', context)

def team_details(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    players = Player.objects.filter(team=team)
    home_matches = Match.objects.filter(home_team=team, date__gte=timezone.now()).order_by('date')
    away_matches = Match.objects.filter(away_team=team, date__gte=timezone.now()).order_by('date')
    matches = (home_matches | away_matches).distinct()
    fixtures = Match.objects.filter(home_team=team, date__gte=timezone.now()).order_by('date')
    home_results =  Result.objects.filter(match__home_team=team).order_by('-match__date')
    away_results =  Result.objects.filter(match__away_team=team).order_by('-match__date')
    results = (home_results | away_results).distinct()

    context = {
        'team': team,
        'players': players,
        'recent_matches': results,
        'fixtures': fixtures,
        'results': results,
        "all_leagues": League.objects.all(),
        "all_seasons": Season.objects.all(),
    }
    return render(request, 'teams/team_details.html', context)

def player_details(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    context = {
        'player': player,
        "all_leagues": League.objects.all(),
        "all_seasons": Season.objects.all(),
    }
    return render(request, 'players/player_details.html', context)

def match_details(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    result = Result.objects.filter(match=match).first()

    context = {
        'match': match,
        'result': result,
        "all_leagues": League.objects.all(),
        "all_seasons": Season.objects.all(),
    }
    return render(request, 'matches/match_details.html', context)

def season_details(request, season_id):
    season = get_object_or_404(Season, pk=season_id)
    leagues = League.objects.filter(season=season)
    matches = Match.objects.filter(league__season=season).order_by('date', 'time')

    context = {
        'season': season,
        'leagues': leagues,
        'recent_matches': matches,
        "all_leagues": League.objects.all(),
        "all_seasons": Season.objects.all(),
    }
    return render(request, 'seasons/season_details.html', context)

def archive(request):
    seasons = Season.objects.all().order_by('-year')
    context = {
        'seasons': seasons,
        "all_leagues": League.objects.all(),
        "all_seasons": Season.objects.all(),
    }
    return render(request, 'seasons/archive.html', context)


