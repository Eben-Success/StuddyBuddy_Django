from django.db import models

# Create your models here.

class Room(models.Model):
    #host = 
    #topic = 
    name = models.CharField(max_length=200)
    # description can be empty, form can be empty while submitting form
    description = models.TextField(null=True, blank=True)
    #participants = 

    # when saved, take a timestamp
    updated = models.DateTimeField(auto_now=True)
    # saves the first time we save an instance
    created = models.DateTimeField(auto_now_add=True)