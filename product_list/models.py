from django.db import models


class Product_Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(
        max_length=250,
        blank=True,
        null=True
        )

    def __str__(self):
        return self.name
