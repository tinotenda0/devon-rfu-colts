from django import forms
from django.db.models import Q

from .models import CustomUser
from app.models import Team, League, Player, LeagueMembership, Result, Season, Standings, Match

class CustomUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "role", "password"]

class ClubAdminCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'club']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.role = 'club_admin'
        if commit:
            user.save()
        return user

class AddTeamForm(forms.ModelForm):
    crest_upload = forms.ImageField(
        label="Or upload a crest",
        required=False,
        widget=forms.FileInput(attrs={'accept': 'image/*'})
    )

    class Meta:
        model = Team
        fields = ['name', 'crest', 'crest_upload', 'team_bio', 'gender', 'age_group']
        labels = {
            'crest': 'Crest URL'
        }
        widgets = {
            'crest': forms.URLInput(attrs={'placeholder': 'https://placehold.co/400x400'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        crest_url = cleaned_data.get('crest')
        crest_upload = cleaned_data.get('crest_upload')

        if crest_url and crest_upload:
            raise forms.ValidationError("Please provide a URL or upload an image, not both.", code='invalid')

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data.get('crest_upload'):
            instance.crest = self.cleaned_data['crest_upload'].url
        if commit:
            instance.save()
        return instance

class AddLeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['name', 'age_group', 'gender', 'season', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age_group': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'season': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class AddSeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['year', 'start_date', 'end_date', 'archived_status']
        widgets = {
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'archived_status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class AddFixtureForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['league', 'season', 'date', 'time', 'venue', 'home_team', 'away_team']
        widgets = {
            'league': forms.Select(attrs={'class': 'form-control'}),
            'season': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'home_team': forms.Select(attrs={'class': 'form-control'}),
            'away_team': forms.Select(attrs={'class': 'form-control'}),
        }

class AddResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = [
            "match",
            "home_score",
            "away_score",
            "home_tries",
            "away_tries",
            "notes",
        ]
        widgets = {
            "match": forms.Select(attrs={"class": "form-control"}),
            "home_score": forms.NumberInput(attrs={"class": "form-control"}),
            "away_score": forms.NumberInput(attrs={"class": "form-control"}),
            "home_tries": forms.NumberInput(attrs={"class": "form-control"}),
            "away_tries": forms.NumberInput(attrs={"class": "form-control"}),
            "notes": forms.TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, team=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        played_matches = Result.objects.values_list('match_id', flat=True)
        queryset = Match.objects.exclude(id__in=played_matches)
        if team:
            queryset = queryset.filter(
                Q(home_team=team) | Q(away_team=team)
            )
        if self.instance and self.instance.pk:
            current_match_id = self.instance.match.id
            queryset = Match.objects.filter(
                Q(id__in=queryset) | Q(id=current_match_id)
            )
        self.fields['match'].queryset = queryset

class AddPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'age', 'position', 'bio', 'privacy_consent']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'privacy_consent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AddPlayerForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user and self.user.club:
            instance.Team = self.user.club
        if commit:
            instance.save()
        return instance
