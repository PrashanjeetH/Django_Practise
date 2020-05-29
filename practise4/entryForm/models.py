from django.db import models

#create your models here

class Product(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    roll_number = models.IntegerField()
