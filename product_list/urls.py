from django.urls import path

from product_list import views

app_name = 'product_list'


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>', views.product_list, name='product_category'),
    path('history/', views.product_list, name='history'),
    path('showroom/', views.product_list, name='showroom'),
]