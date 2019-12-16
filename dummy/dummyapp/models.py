from django.db import models

# Create your models here.

class Imagemodel(models.Model):
    name=models.CharField(max_length=264)
    email=models.EmailField()
    image=models.ImageField(upload_to='images/')