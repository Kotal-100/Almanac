from django.db import models

# Create your models here.
class Blog(models.Model):
 sakumono = models.CharField(max_length=200)
 military = models.TextField()
 maps = models.TextField()
 village= models.TextField()
 sanitation = models.TextField()
 mine = models.TextField()
 
def __str__(self):
        return self.sakumono
 