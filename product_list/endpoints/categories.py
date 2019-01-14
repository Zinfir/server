from django.urls import path

from product_list.api import (
    rest_category_list
    )

app_name = 'rest_product_list'


urlpatterns = [
    path('', rest_category_list, name='rest_list'),
]