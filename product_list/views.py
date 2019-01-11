import json

from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from product_list.models import Product_Category
from product_detail.models import Product
from product_list.forms import Category_Form

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
    products += Product.objects.filter(pk__gt=22)
    products += Product.objects.filter(name='Red Iron Chair')
    products += Product.objects.filter(name='Wooden Arm Chair')
    

    context["product_list_products"] = products

    categories_menu_links = get_list_or_404(Product_Category)

    context["categories_menu_links"] = categories_menu_links

    obj = get_object_or_404(Product_Category, pk=pk)

    context["instance"] = obj

    return render(request, "product_list/product_list.html", context)


def category_detail(request, pk):

    obj = get_object_or_404(Product_Category, pk=pk)

    return render(request, "product_list/category_detail.html", {'instance': obj})

def category_create(request):

    template_name = "product_list/category_create.html"
    success_url = reverse_lazy('product_list:product_category', kwargs={'pk': 1})
    form = Category_Form(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, template_name, {'form': form})

def category_update(request, pk):

    template_name = "product_list/category_create.html"
    success_url = reverse_lazy('product_list:category_detail', kwargs={'pk': pk})
    cat = get_object_or_404(Product_Category, pk=pk)
    form = Category_Form(instance=cat)

    if request.method == 'POST':
        form = Category_Form(
            request.POST,
            instance=cat
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, template_name, {'form': form})

def category_delete(request, pk):

    template_name = "product_list/category_delete.html"
    success_url = reverse_lazy('product_list:product_category', kwargs={'pk': 1})
    obj = get_object_or_404(Product_Category, pk=pk)

    if request.method == 'POST':
        obj.delete()

        return redirect(success_url)

    return render(request, template_name, {'instance': obj})


def category_list(request):

    list = get_list_or_404(Product_Category)

    return render(request, "product_list/category_list.html", {"list": list})