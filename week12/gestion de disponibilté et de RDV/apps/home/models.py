

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.

class liste(models.Model):
    name = models.CharField(max_length=30)
    agent_name = models.CharField(max_length=40)
    email = models.EmailField()
    agent_grade = models.CharField(max_length=30)
    comment = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.name} {self.agent_name} {self.email} {self.agent_grade} {self.comment}'

class agent(models.Model):
    name = models.CharField(max_length=30)
    grade = models.CharField(max_length=40)
    status = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.name} {self.grade} {self.status} '

