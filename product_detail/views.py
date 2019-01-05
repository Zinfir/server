from django.shortcuts import render

def product_detail(request):

    links_menu = {
        'links' : [
            { 'href' : 'main:main' , 'name' : 'main' },
            { 'href' : 'product_list:product_list' , 'name' : 'product_list' },
            { 'href' : 'product_list:history' , 'name' : 'history' },
            { 'href' : 'product_list:showroom' , 'name' : 'showroom' },
            { 'href' : 'contacts:contacts' , 'name' : 'contacts' },
        ],
        'sub_links' : [
            { 'href' : 'product_detail:all' , 'name' : 'all' },
            { 'href' : 'product_detail:home' , 'name' : 'home' },
            { 'href' : 'product_detail:office' , 'name' : 'office' },
            { 'href' : 'product_detail:modern' , 'name' : 'modern' },
            { 'href' : 'product_detail:furniture' , 'name' : 'furniture' },
            { 'href' : 'product_detail:classic' , 'name' : 'classic' },
        ],
        'content' : [
            'fishnet chair',
            'another chair',
        ]
    }

    return render(request, "product_detail/product_detail.html", links_menu)