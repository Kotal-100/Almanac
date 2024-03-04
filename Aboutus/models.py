from django.db import models

# Create your models here.

class AboutUs(models.Model):
 title = models.CharField(max_length=200)
 description = models.TextField(null=True,blank=True)
 our_mission = models.TextField()
 our_vision = models.TextField()
 why_us = models.TextField()
 meet_our_team = models.TextField()
 
 def __str__(self):
        return self.title