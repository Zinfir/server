from django.shortcuts import render

def product_list(request):

    links_main_menu = {
        'links' : [
            { 'href' : 'main:main' , 'name' : 'main' },
            { 'href' : 'product_list:product_list' , 'name' : 'product_list' },
            { 'href' : 'product_list:history' , 'name' : 'history' },
            { 'href' : 'product_list:showroom' , 'name' : 'showroom' },
            { 'href' : 'contacts:contacts' , 'name' : 'contacts' },
        ],
    }

    return render(request, "product_list/product_list.html", links_main_menu)
