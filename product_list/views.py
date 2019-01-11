import json

from django.shortcuts import render, get_list_or_404, get_object_or_404

from product_list.models import Product_Category
from product_detail.models import Product

def product_list(request, pk):

    context = {}

    with open('data/context.json') as file:
        context = json.load(file)

    products = []
    products += Product.objects.filter(name='Hanging Lamp')
    products += Product.objects.filter(name='White Arm Chair')
    products += Product.objects.filter(name='Table Lamp')
    products += Product.objects.filter(name='Wall Lamp')
    products += Product.objects.filter(name='Mortar and Pestle')
    products += Product.objects.filter(name='White Vase')
    products += Product.objects.filter(name='Red Iron Chair')
    products += Product.objects.filter(name='Wooden Arm Chair')

    context["product_list_products"] = products

    categories_menu_links = get_list_or_404(Product_Category)

    context["categories_menu_links"] = categories_menu_links

    obj = get_object_or_404(Product_Category, pk=pk)

    context["instance"] = obj

    return render(request, "product_list/product_list.html", context)
