from django.db import models

# Create your models here.


class Slider(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.Title
