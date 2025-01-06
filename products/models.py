from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField()
    affiliate_link = models.URLField()

    def __str__(self):
        return self.name
