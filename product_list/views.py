import json

from django.shortcuts import render

def product_list(request):

    context = {}

    with open('data/context.json') as file:
        context = json.load(file)

    return render(request, "product_list/product_list.html", context)
