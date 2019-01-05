from django.shortcuts import render

def product_list(request):

    links_menu = {
        'links' : [
            { 'href' : 'main:main' , 'name' : 'main' },
            { 'href' : 'product_list:product_list' , 'name' : 'product_list' },
            { 'href' : 'product_list:history' , 'name' : 'history' },
            { 'href' : 'product_list:showroom' , 'name' : 'showroom' },
            { 'href' : 'contacts:contacts' , 'name' : 'contacts' },
        ],
        'sub_links' : [
            { 'href' : 'product_list:all' , 'name' : 'all' },
            { 'href' : 'product_list:home' , 'name' : 'home' },
            { 'href' : 'product_list:office' , 'name' : 'office' },
            { 'href' : 'product_list:modern' , 'name' : 'modern' },
            { 'href' : 'product_list:furniture' , 'name' : 'furniture' },
            { 'href' : 'product_list:classic' , 'name' : 'classic' },
        ],
        'content' : [
            'fishnet chair',
            'another chair',
        ]
    }

    return render(request, "product_list/product_list.html", links_menu)
