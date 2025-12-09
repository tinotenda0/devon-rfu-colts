from django.shortcuts import render, redirect, get_object_or_404
from accounts.decorators import admin_required
from .models import Season, League, Result
from .forms import SeasonForm

# Create your views here.

def navbar_link_data(request):
    all_leagues = League.objects.all()
    return {"all_leagues": all_leagues}

def index_page_data(request):
    recent_matches = Match.objects.all().order_by('-date')[:4]
    upcoming_fixtures = Match.objects.filter(date__gte=timezone.now()).order_by('date')[:4]
    return {
        "recent_matches": recent_matches,
        "upcoming_fixtures": upcoming_fixtures,
    }

from django.utils import timezone
from app.models import Match

def index(request):
    context = {
        "all_leagues": League.objects.all(),
        "all_seasons": Season.objects.filter(archived_status=False),
        "recent_matches": Result.objects.select_related('match').order_by('-match__date')[:4],
        "fixtures": Match.objects.filter(date__gte=timezone.now()).order_by('date')[:4],
    }
    return render(request, "index.html", context=context)


def table(request):
    return render(request, "table.html")


def matches(request):
    context = {
        "all_leagues": League.objects.all(),
        "all_seasons": Season.objects.filter(archived_status=False),
        "recent_matches": Result.objects.select_related('match').order_by('-match__date')[:4],
        "fixtures": Match.objects.filter(date__gte=timezone.now()).order_by('date')[:4],
    }
    return render(request, "matches/matches.html", context=context)


def about(request):
    all_leagues = League.objects.all()
    all_seasons = Season.objects.filter(archived_status=False)
    return render(request, "about.html", {"all_leagues": all_leagues, "all_seasons": all_seasons})


def auth(request):
    return render(request, "auth.html")

def contact(request):
    all_leagues = League.objects.all()
    all_seasons = Season.objects.filter(archived_status=False)
    return render(request, "contact.html", {"all_leagues": all_leagues, "all_seasons": all_seasons})