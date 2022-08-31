from django.db import models
from django.urls import reverse

# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'toy_id': self.id})

PIECES = (
    ('W', 'Weapon'),
    ('I', 'Interchangeable body piece'),
    ('B', 'Bonus piece to build a special character')
)

class Piece(models.Model):
    piece = models.CharField(
        max_length=10,
        choices = PIECES,
        default = PIECES [0][0]
        )
    toy = models.ForeignKey(Toy, on_delete = models.CASCADE)

class Ability(models.Model):
    description = models.CharField(max_length=100)    

    toy = models.ForeignKey(Toy, on_delete=models.CASCADE)

    