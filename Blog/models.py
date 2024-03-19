from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
class Blog(models.Model):
 sakumono = models.CharField(max_length=200)
 military = models.TextField()
 maps = models.TextField()
 village= models.TextField()
 sanitation = models.TextField()
 mine = models.TextField()
 image = models.ImageField(upload_to='assets/image',null=True, blank=True)
def __str__(self):
        return self.sakumono
 