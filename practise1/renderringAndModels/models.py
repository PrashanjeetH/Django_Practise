from django.db import models

# Create your models here.
class Students(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    roll_no = models.IntegerField()

    def __str__(self):
        return f"{self.id} | {self.fname} {self.lname} || Roll Number = {self.roll_no}" 
