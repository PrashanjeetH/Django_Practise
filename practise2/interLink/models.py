from django.db import models

# Create your models here.
class Datalist(models.Model):
    fname = models.CharField(max_length = 50)
    mname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.id}|{self.fname} {self.mname} {self.lname}"

class Contact(models.Model):
    fname = models.ForeignKey(Datalist, on_delete=models.CASCADE, related_name = "firstname")
    no = models.IntegerField()
    email = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.fname} | {self.no} :: {self.email} "
