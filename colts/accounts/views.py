from django.shortcuts import render, redirect
from .forms import CustomUserRegistrationForm, ClubAdminCreationForm, AddTeamForm
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
            return redirect("dashboard")
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
            return redirect("dashboard")
    else:
        form = AddTeamForm()
    return render(request, "accounts/new_team.html", {"form": form})

@club_admin_required
def edit_team(request, team_id):
    # This view now only processes the form submission and redirects.
    team = Team.objects.get(id=team_id, pk=request.user.club.pk) # Security check
    if request.method == 'POST':
        form = AddTeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
    # Redirect back to the dashboard whether the form is valid or not.
    # Invalid form state will be handled by the club_admin_dash view on the next GET request.
    return redirect('club_admin_dash')