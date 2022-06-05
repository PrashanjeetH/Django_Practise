from django.db import models

# Create your models here.
class StudentsModel(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    city = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    def __str__(self):
        return f"{self.name} || {self.roll_no}"
