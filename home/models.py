from django.db import models

# Create your models here.


class Photo(models.Model):
    file = models.FileField(upload_to='file')


class Image(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/%y')

    def __str__(self):
        return self.caption
