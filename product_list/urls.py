from django.urls import path

from product_list.views import product_list, category_detail, category_create, category_update, category_delete, category_list

app_name = 'product_list'


urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:pk>', product_list, name='product_category'),
    path('history/', product_list, name='history'),
    path('showroom/', product_list, name='showroom'),
    path('detail/<int:pk>', category_detail, name='category_detail'),
    path('delete/<int:pk>', category_delete, name='category_delete'),
    path('update/<int:pk>', category_update, name='category_update'),
    path('create/', category_create, name='category_create'),
    path('category_list/', category_list, name='category_list'),
]