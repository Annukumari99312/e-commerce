from django.db import models

# Create your models here.


class Blogcategory(models.Model):
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name


class Blogs(models.Model):
    Title = models.CharField(max_length=50)
    Small_content = models.TextField()
    Large_content = models.TextField()
    Small_image = models.ImageField(upload_to='pics')
    Large_image = models.ImageField(upload_to='pics')
    Category = models.ForeignKey(Blogcategory, on_delete=models.PROTECT, default=1)
    Author = models.CharField(max_length=20)
    Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Title
