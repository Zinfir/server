"""
Контроллер для страницы детального описания продукта
"""
import json

from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from product_list.models import Product_Category
from product_detail.models import Product


def product_detail(request, pk):
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

    products = []
    products += Product.objects.filter(name='Hanging Lamp')
    products += Product.objects.filter(name='White Arm Chair')
    products += Product.objects.filter(name='Table Lamp')
    products += Product.objects.filter(pk=pk)

    context["product_detail_products"] = products

    categories_menu_links = []

    categories_menu_links += Product_Category.objects.all()

    context["categories_menu_links"] = categories_menu_links

    

    obj = get_object_or_404(Product, pk=pk)

    context["instance"] = obj

    return render(request, "product_detail/product_detail.html", context)
