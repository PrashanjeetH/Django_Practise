"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UsersDataModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    firstName = models.CharField(max_length=100, name="FirstName")
    lastName = models.CharField(max_length=100, name="LastName")
    male = 1
    female = 2
    other = 3
    gender_choice = [
        (male, "Male"),
        (female, "Female"),
        (other, "Other")
    ]
    gender = models.IntegerField(choices=gender_choice, default=male)
    email = models.EmailField(unique=True)
    number = models.IntegerField(verbose_name="Contact No.")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Users Data"
        verbose_name = "User Data"

    def __str__(self):
        return f"{self.FirstName}{self.LastName}"

    def delete(self, *args, **kwargs):
        self.username.delete()
        super().delete(*args, **kwargs)

