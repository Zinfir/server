"""
Контроллер для страницы детального описания продукта
"""
import json

from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, 
    UpdateView, DeleteView
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from product_list.models import Product_Category
from product_detail.models import Product
from product_detail.forms import Product_Form


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

    context["product_detail_products"] = products

    categories_menu_links = get_list_or_404(Product_Category)

    context["categories_menu_links"] = categories_menu_links

    obj = get_object_or_404(Product, pk=pk, is_active=True)
    context["instance"] = obj

    return render(request, "product_detail/product_detail.html", context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "product_detail/product_create.html"
    form_class = Product_Form
    success_url = reverse_lazy('product_list:product_category', kwargs={'pk': 1})
    login_url = reverse_lazy('accounts:login')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    queryset = Product.objects.filter(is_active=True)
    template_name = "product_detail/product_create.html"
    form_class = Product_Form
    success_url = reverse_lazy('product_list:product_category', kwargs={'pk': 1})
    login_url = reverse_lazy('accounts:login')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Product.objects.filter(is_active=True)
    template_name = 'product_detail/product_delete.html'
    success_url = reverse_lazy('product_list:product_category', kwargs={'pk': 1})
    login_url = reverse_lazy('accounts:login')


def product_create(request):

    template_name = "product_detail/product_create.html"
    success_url = reverse_lazy('product_list:product_category', kwargs={'pk': 1})
    form = Product_Form(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, template_name, {'form': form})


def product_update(request, pk):
    template_name = "product_detail/product_create.html"
    success_url = reverse_lazy('product_detail:product_detail', kwargs={'pk': pk})
    prod = get_object_or_404(Product, pk=pk)
    form = Product_Form(instance=prod)

    if request.method == 'POST':
        form = Product_Form(
            request.POST,
            instance=prod
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, template_name, {'form': form})


@login_required(login_url=reverse_lazy('accounts:login'))
def product_delete(request, pk):
    template_name = "product_detail/product_delete.html"
    success_url = reverse_lazy('product_list:product_category', kwargs={'pk': 1})
    obj = get_object_or_404(Product, pk=pk, is_active=True)

    if request.method == 'POST':
        obj.is_active = False

        obj.save()

        return redirect(success_url)

    return render(request, template_name, {'instance': obj})