from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=200)
    problem_statemant = models.CharField(max_length=1000)
    unfair_advantage = models.CharField(max_length=1000)
    target_audience = models.CharField(max_length=200)
    num_of_customers = models.IntegerField()
    revenue = models.DecimalField(max_digits = 4, decimal_places=2)
    
    def __str__(self):
        return str(self.name)


class Scoping_Block(models.Model):
    phase_number = models.IntegerField()
    phase_name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.phase_name)

class High_Level_Task(models.Model):
    task = models.CharField(max_length=200)
    scope = models.ForeignKey(Scoping_Block, blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.task)

class Progress_Block(models.Model):
    hours = models.DecimalField(max_digits = 4, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=1000)
    high_level_purpose = models.CharField(max_length=1000)
    scoping_phase = models.ForeignKey(Scoping_Block, blank=True, null=True, on_delete=models.CASCADE)
    #scope_retrieve = Scoping_Block.objects.get(phase_name=scoping_phase.phase_name)
    #high_level_task = models.ForeignKey(High_Level_Task, blank=True, null=True, on_delete=models.CASCADE, limit_choices_to={'scope_id': scope_retrieve.id})
    high_level_task = models.ForeignKey(High_Level_Task, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)