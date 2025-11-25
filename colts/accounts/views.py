from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserRegistrationForm, ClubAdminCreationForm, AddTeamForm, AddLeagueForm, AddSeasonForm, AddFixtureForm, AddPlayerForm
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
def dashboard(request):
    seasons = Season.objects.all().order_by("-start_date")
    leagues = League.objects.all()
    teams = Team.objects.all()
    club_admins = CustomUser.objects.filter(role="club_admin")
    matches = Match.objects.all().order_by("-date")[:10]

    context = {
        "seasons": seasons,
        "leagues": leagues,
        "teams": teams,
        "club_admins": club_admins,
        "matches": matches,
    }
    return render(request, "accounts/dashboard.html", context)

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
    return render(request, "accounts/new_team.html", {"form": form})

@club_admin_required
def edit_team(request, team_id):
    team = Team.objects.get(id=team_id, pk=request.user.club.pk)
    if request.method == 'POST':
        form = AddTeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
    return redirect('club_admin_dash')

@club_admin_required
def new_league(request):
    if request.method == "POST":
        form = AddLeagueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AddLeagueForm()
    return render(request, "accounts/new_league.html", {"form": form})

@club_admin_required
def new_season(request):
    if request.method == "POST":
        form = AddSeasonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AddSeasonForm()
    return render(request, "accounts/new_season.html", {"form": form})

@club_admin_required
def new_fixture(request):
    if request.method == "POST":
        form = AddFixtureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AddFixtureForm()
    return render(request, "accounts/new_fixture.html", {"form": form})

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
    return render(request, "accounts/new_player.html", {"form": form})

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
    matches_in_league = Match.objects.filter(league=league).order_by('date', 'time')
    standings = calculate_standings(league)

    context = {
        'league': league,
        'teams_in_league': teams_in_league,
        'matches_in_league': matches_in_league,
        'standings': standings,
    }
    return render(request, 'leagues/league_details.html', context)

def team_details(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    players = Player.objects.filter(team=team)
    home_matches = Match.objects.filter(home_team=team).order_by("-date")
    away_matches = Match.objects.filter(away_team=team).order_by("-date")
    matches = (home_matches | away_matches).distinct().order_by("-date")[:10]

    context = {
        'team': team,
        'players': players,
        'matches': matches,
    }
    return render(request, 'teams/team_details.html', context)

def player_details(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    context = {
        'player': player,
    }
    return render(request, 'players/player_details.html', context)

def match_details(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    result = Result.objects.filter(match=match).first()

    context = {
        'match': match,
        'result': result,
    }
    return render(request, 'matches/match_details.html', context)

def season_details(request, season_id):
    season = get_object_or_404(Season, pk=season_id)
    leagues = League.objects.filter(season=season)
    matches = Match.objects.filter(league__season=season).order_by('date', 'time')

    context = {
        'season': season,
        'leagues': leagues,
        'matches': matches,
    }
    return render(request, 'seasons/season_details.html', context)

def archive(request):
    seasons = Season.objects.all().order_by('-year')
    context = {
        'seasons': seasons,
    }
    return render(request, 'seasons/archive.html', context)


