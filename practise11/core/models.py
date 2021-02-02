from django.db import models

# Create your models here.

class Person(models.Model):
    FirstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class Student(Person):
    std = models.CharField(max_length=10)

class Teacher(Person):
    number = models.IntegerField()
