from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from django.template import Template, Context

import json


def index(request):

    context = {}

    with open('data/context.json') as file:
        context = json.load(file)

    return render(request, 'main/index.html', context)
