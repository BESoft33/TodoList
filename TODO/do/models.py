from django.db import models
from datetime import date

#Database

class Assignment(models.Model):

    title = models.CharField(max_length=255)
    assigned_on = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title 
