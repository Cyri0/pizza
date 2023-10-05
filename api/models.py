from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=2000)

    img = models.ImageField(upload_to="static/images/pizzas/", blank=True, null=True)

    def __str__(self):
        return self.name + " (" + str(self.price) + "Ft)"

    def serializer(self):
        return {
            "name":self.name,
            "price":self.price,
            "img": str(self.img)
        }