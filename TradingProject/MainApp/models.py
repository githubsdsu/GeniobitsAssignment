from django.db import models

# Create your models here.
class Index(models.Model):
    timeframe=models.IntegerField(default=None)
    csvfile=models.FileField(upload_to='files/',default=False)
