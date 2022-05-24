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

class BusinessModel(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    pincode = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return redirect('profiles')
    
    def save(self, *args, **kwargs):

        if len(str(self.pincode)) > 6:
            raise Exception('Maximum Length of pincode must not exceed 6.')
        else:
            return super(BusinessModel, self).save(*args, **kwargs)
            

