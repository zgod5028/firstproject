from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Car(models.Model):
    title = models.CharField(max_length=1000)
    model = models.CharField(max_length=1000)
    year = models.IntegerField()
    image = models.ImageField(upload_to='media/car_images')
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Если нужна точность

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.title
