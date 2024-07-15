from django.db import models

# Create your models here.

class Recipie(models.Model):
    recipie_name = models.CharField(max_length=100)
    recipie_description = models.TextField()
    recipie_image = models.ImageField(upload_to="recipie")


