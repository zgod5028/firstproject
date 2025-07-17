from django.db import models

class category(models.Model):
    titel = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.titel
    
    
    class Car(models.Model):
        title = models.CharField(max_length=1000)
        model = models.CharField(max_length=1000)
        year = models.IntegerField()
        image = models.ImageField(upload_to='media/cart_images')
        price = models.IntegerField(decimal_places=1000)
        
        def __str__(self):
            return self.title


class Car:
    pass