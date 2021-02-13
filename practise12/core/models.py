from django.db import models

# Create your models here.
class StudentModel(models.Model):

    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    roll_no = models.IntegerField(unique=True)


    def __str__(self):
        return self.firstname
