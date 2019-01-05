from django.urls import path

from product_detail import views


app_name = 'product_detail'

urlpatterns = [
    path('', views.product_detail, name='product_detail'),
    path('all/', views.product_detail, name='all'),
    path('home/', views.product_detail, name='home'),
    path('office/', views.product_detail, name='office'),
    path('modern/', views.product_detail, name='modern'),
    path('furniture/', views.product_detail, name='furniture'),
    path('classic/', views.product_detail, name='classic'),
]