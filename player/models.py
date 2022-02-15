from django.db import models

# Create your models here.
class Player(models.Model):
    guess = models.CharField(max_length = 5)
    letterscorrect = models.CharField(max_length = 5)
    win = models.BooleanField(default = False)
    wordlist = models.JSONField(null = True)


