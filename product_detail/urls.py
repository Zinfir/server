from django.urls import path

from product_detail import views


app_name = 'product_detail'

urlpatterns = [
    path('<int:pk>/', views.product_detail, name='product_detail'),
]