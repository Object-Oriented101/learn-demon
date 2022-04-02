from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class Progress_Block(models.Model):
    time = models.DecimalField(max_digits = 4, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=1000)


class Project(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)
    week_number = models.CharField(max_length=2, blank=True)
    end_date = models.DateField()

    def __str__(self):
        return str(self.name)
    
    def save(self,*args, **kwargs):
        print(self.start_date.isocalendar()[1])
        if self.week_number == "":
            self.week_number = self.start_date.isocalendar()[1] 
        super().save(*args, **kwargs)

class Investor(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    college = models.CharField(max_length=200)
    net_worth = models.IntegerField()

    def __str__(self):
        return str(self.name)