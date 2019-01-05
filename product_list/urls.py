from django.urls import path

from product_list import views

app_name = 'product_list'


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('history/', views.product_list, name='history'),
    path('showroom/', views.product_list, name='showroom'),
    path('all/', views.product_list, name='all'),
    path('home/', views.product_list, name='home'),
    path('office/', views.product_list, name='office'),
    path('modern/', views.product_list, name='modern'),
    path('furniture/', views.product_list, name='furniture'),
    path('classic/', views.product_list, name='classic'),
]