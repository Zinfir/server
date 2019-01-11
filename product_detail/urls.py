from django.urls import path

from product_detail.views import product_detail, product_create, product_update, product_delete


app_name = 'product_detail'

urlpatterns = [
    path('<int:pk>/', product_detail, name='product_detail'),
    path('create/', product_create, name='create'),
    path('update/<int:pk>/', product_update, name='update'),
    path('delete/<int:pk>/', product_delete, name='delete')
]