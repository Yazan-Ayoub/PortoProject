from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    Titel=models.TextField(max_length=100)
    summary = models.CharField(max_length=500)

