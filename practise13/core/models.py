from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
GenderChoices = (
    ('M','Male'),
    ('F','Female'),
    ('O', 'Others'),
)
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length =1, choices=GenderChoices)
    bio = models.CharField(max_length = 50)
    contact = models.PositiveBigIntegerField()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return redirect('profiles')