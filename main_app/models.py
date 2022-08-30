from django.db import models
from django.urls import reverse

# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

def get_absolute_url(self):
    return reverse('detail', kwargs={'toy_id': self.id})
    

    