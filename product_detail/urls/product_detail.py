from django.urls import path

from product_detail.views import (
    product_detail, product_create, product_update, product_delete,
    ProductCreateView, ProductUpdateView, ProductDeleteView,
    )


app_name = 'product_detail'

urlpatterns = [
    path('<int:pk>/', product_detail, name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', product_delete, name='delete')
]