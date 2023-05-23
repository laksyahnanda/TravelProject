from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
#
# class Destinations(models.Model):
#     name:models.Charfield(max_length=200)
#     img:models.ImageField(upload_to='photos')
#     desc:models.TextField()

    def __str__(self):
        return self.name
