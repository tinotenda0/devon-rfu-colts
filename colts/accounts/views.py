from django.shortcuts import render, redirect
from .forms import CustomUserRegistrationForm, ClubAdminCreationForm
from django.contrib.auth import login
from accounts.decorators import admin_required
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
    matches = Match.objects.all().order_by("-date")[:10]  # Recent 10

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
            return redirect("dashboard")
    else:
        form = ClubAdminCreationForm()
    return render(request, "accounts/add_new.html", {"form": form, "clubs": clubs})


@club_admin_required
def club_admin_dash(request):
    club = request.user.club
    players = Player.objects.filter(team=club)

    home_matches = Match.objects.filter(home_team=club).order_by("-date")
    away_matches = Match.objects.filter(away_team=club).order_by("-date")
    matches = (home_matches | away_matches).distinct().order_by("-date")[:10]

    context = {
        "club": club,
        "players": players,
        "matches": matches,
    }
    return render(request, "accounts/club_admin_dash.html", context)
