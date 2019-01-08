from django.db import models

from product_list.models import Product_Category


class Product(models.Model):
    product_category = models.ForeignKey(
        Product_Category,
        on_delete = models.CASCADE
        )
    name = models.CharField(
        verbose_name = 'имя продукта',
        max_length = 128
        )
    image = models.ImageField(
        upload_to = 'products_images', 
        blank = True
        )
    short_desc = models.CharField(
        verbose_name = 'краткое описание',
        max_length = 60,
        blank = True
        )
    description = models.TextField(
        verbose_name = 'описание',
        blank = True
        )
    special_offer = models.CharField(
        verbose_name = 'специальное предложение',
        max_length = 50,
        blank = True,
        null = True
        )
    price = models.DecimalField(
        verbose_name = 'цена',
        max_digits = 8, 
        decimal_places = 2, 
        default = 0
        )
    quantity = models.PositiveIntegerField(
        verbose_name = 'склад',
        default = 0
    )


    def __str__(self):
        return "{} ({})".format(self.name, self.product_category.name)
