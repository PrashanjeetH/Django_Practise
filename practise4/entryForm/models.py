from django.db import models

# Create your models here.

class Form(models.Model):
    MAlE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MAlE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    fname = models.CharField(max_length = 20)
    mname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    gender = models.CharField(
            max_length=1,
            choices=GENDER_CHOICES,
            default=MAlE,)
    dob = models.DateField()
    no = models.IntegerField()
    email = models.CharField(max_length = 20)
    address = models.CharField(max_length = 200)

    def __str__(self):
        return f"{self.id} | {self.fname} {self.mname} {self.lname} |/|\| {self.dob}:: {self.gender}"
