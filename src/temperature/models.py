from django.db import models

class TempReading(models.Model):
    value = models.DecimalField( max_digits=5, decimal_places=2)
    date = models.DateTimeField()
