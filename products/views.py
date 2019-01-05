from django.shortcuts import render


def products(request):

    context = {
        'results':[
            'apple',
            'banana',
            'apricot',
            False,
            False,
            False,
            'apple',
            'banana',
            'apricot',
        ]
    }
    
    return render(request, "products/list.html", context)


def detail(request, pk):

    context = {
        'results':[
            'apple',
            'banana',
            'apricot',
            False,
            False,
            False,
            'apple',
            'banana',
            'apricot',
        ]
    }

    return render(
        request, 
        "products/detail.html", 
        {'instance': context['results'][pk]}
    )


def create(request):

    return render(request, "products/create.html", {})
