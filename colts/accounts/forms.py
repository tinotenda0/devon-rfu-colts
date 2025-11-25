from django import forms
from .models import CustomUser
from app.models import Team

class CustomUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "role", "password"]


class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email"]

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
