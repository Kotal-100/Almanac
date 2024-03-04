from django.db import models

# Create your models here.

class AboutUs(models.Model):
 title = models.CharField(max_length=200)
 our_mission = models.TextField()
 our_vision = models.TextField()
 why_us = models.TextField()
 meet_our_team = models.TextField()