from django.db import models
from django.http import HttpResponse, JsonResponse
# Create your models here.#



class Contactus(models.Model):
 name = models.TextField()
 email= models.TextField()
 message = models.TextField()
 def __str__(self):
        return self.name