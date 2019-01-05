from django.urls import path

from products import views


app_name = 'products'

urlpatterns = [
    path('', views.products, name='list'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
]