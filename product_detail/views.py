"""
Контроллер для страницы детального описания продукта
"""
import json

from django.shortcuts import render

from product_list.models import Product_Category
from product_detail.models import Product


def product_detail(request):
    """
    Рендеринг страницы детального описания продукта

    Args:
        request (str): запрос пользователя

    Returns:
        product_detail.html: страница html с подробным описанием товара
    """
    context = {}

    with open('data/context.json') as file:
        context = json.load(file)

    context["products"] = Product.objects.all()[:4]

    return render(request, "product_detail/product_detail.html", context)
