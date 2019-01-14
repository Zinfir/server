import json
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from product_list.models import Product_Category
from django.http import HttpResponse, JsonResponse


def rest_category_list(request):
    query = get_list_or_404(Product_Category)
    data = map(
        lambda itm: {
            'name': itm.name,
            'description': itm.description,
            'modified': itm.modified,
            'created': itm.created
        },
        query
    )

    return JsonResponse(
        {
        'results': list(data)
        }
    )
