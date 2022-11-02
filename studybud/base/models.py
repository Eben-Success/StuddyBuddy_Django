from django.db import models

# Create your models here.

class Room(models.Model):
    #host = 
    #topic = 
    name = models.CharField(max_length=200)
    # description can be empty, form can be empty while submitting form
    description = models.TextField(null=True, blank=True)
