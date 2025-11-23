from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("club_admin", "Club Admin"),
        # ('fan', 'Fan'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    club = models.ForeignKey(
        "app.Team", null=True, blank=True, on_delete=models.SET_NULL
    )

    def is_admin(self):
        return self.role == "admin"

    def is_club_admin(self):
        return self.role == "club_admin"
