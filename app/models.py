from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100, default="Unknown")
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
