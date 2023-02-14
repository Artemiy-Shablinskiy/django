from django.db import models
class Contestant(models.Model):
    number = models.PositiveSmallIntegerField()
    time = models.DurationField()
    def __str__(self):
        return f"Contestant {self.number}: {self.time}"
# Create your models here.
