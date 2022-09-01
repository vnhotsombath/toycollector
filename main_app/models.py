from django.db import models
from django.urls import reverse

# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    
    

    def get_absolute_url(self):
        return reverse('detail', kwargs={'toy_id': self.id})

class Ability(models.Model):
    date = models.DateField(null=True)
    description = models.CharField(max_length=100)

    toy = models.ForeignKey(Toy, on_delete=models.CASCADE, null=True) 

    def __str__(self):
        return self.description
    
    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('abilities_detail', kwargs={'pk': self.id})

PIECES = (
    ('W', 'Weapon'),
    ('I', 'Interchangeable body piece'),
    ('B', 'Bonus piece to build a special character')
)

class Piece(models.Model):
    date = models.DateField(null=True)
    piece = models.CharField(
        max_length=1,
        choices = PIECES,
        default = PIECES [0][0]
        )
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_piece_display()} on {self.date}"
    class Meta:
        ordering = ['-date']



