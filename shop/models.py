from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    stock = models.PositiveSmallIntegerField(default=0)
    price = models.IntegerField(default=0)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)


    def __str__(self):
        return self.title
