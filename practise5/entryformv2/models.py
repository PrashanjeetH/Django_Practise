from django.db import models

# Create your models here.

class Signupmodel(models.Model):
    fname = models.CharField(max_length = 50)
    mname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    no = models.IntegerField()
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 200)


    def __str__(self):
        return f"{self.fname}:: {self.fname}:: {self.mname}:: {self.lname}:: {self.no}:: {self.email}:: {self.password}"
