from django.shortcuts import render, redirect
from .forms import CustomUserRegistrationForm
from django.contrib.auth import login
from .decorators import role_required
from .forms import CustomUserEditForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "accounts/index.html")


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


@role_required(["admin", "official"])
def admin_panel(request):
    return render(request, "accounts/admin_panel.html")


@login_required
def profile(request):
    return render(request, "accounts/profile.html", {"user": request.user})


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = CustomUserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = CustomUserEditForm(instance=request.user)
    return render(request, "accounts/edit_profile.html", {"form": form})
