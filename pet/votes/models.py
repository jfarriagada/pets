from django.db import models

VOTES_CHOICES = (
    (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
)

class Pet(models.Model):
    nickname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    photo = models.ImageField(max_length=100, null=True, upload_to='static/img/pets/', blank=True)
    votes = models.IntegerField(default=1, choices = VOTES_CHOICES)
    
    def __str__(self):
        return self.name