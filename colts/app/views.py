from django.shortcuts import render, redirect, get_object_or_404
from accounts.decorators import admin_required
from .models import Season, League, Result
from .forms import SeasonForm

# Create your views here.



@admin_required
def season_list(request):
    seasons = Season.objects.all().order_by('-start_date')
    return render(request, 'seasons/season_list.html', {'seasons': seasons})

@admin_required
def season_add(request):
    if request.method == 'POST':
        form = SeasonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('season_list')
    else:
        form = SeasonForm()
    return render(request, 'seasons/season_form.html', {'form': form, 'action': 'Add'})

@admin_required
def season_edit(request, season_id):
    season = get_object_or_404(Season, pk=season_id)
    if request.method == 'POST':
        form = SeasonForm(request.POST, instance=season)
        if form.is_valid():
            form.save()
            return redirect('season_list')
    else:
        form = SeasonForm(instance=season)
    return render(request, 'seasons/season_form.html', {'form': form, 'action': 'Edit', 'season': season})

@admin_required
def season_delete(request, season_id):
    season = get_object_or_404(Season, pk=season_id)
    if request.method == 'POST':
        season.delete()
        return redirect('season_list')
    return render(request, 'seasons/season_confirm_delete.html', {'season': season})

@admin_required
def season_archive(request, season_id):
    season = get_object_or_404(Season, pk=season_id)
    season.archived_status = True
    season.save()
    return redirect('season_list')

@admin_required
def season_unarchive(request, season_id):
    season = get_object_or_404(Season, pk=season_id)
    season.archived_status = False
    season.save()
    return redirect('season_list')

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
        # "recent_matches": Result.objects.all(),
        # "recent_matches": Match.objects.all().order_by('date')[:4],
        "recent_matches": Result.objects.select_related('match').order_by('-match__date')[:4],
        "upcoming_fixtures": Match.objects.filter(date__gte=timezone.now()).order_by('date')[:4],

    }
    return render(request, "index.html", context=context)


def table(request):
    return render(request, "table.html")


def matches(request):
    return render(request, "matches.html")


def about(request):
    return render(request, "about.html")


def auth(request):
    return render(request, "auth.html")


