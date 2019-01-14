from django.urls import path

from product_list.views import (
    product_list, category_detail,
    category_create, category_update,
    category_delete, category_list, CategoryDetailView,
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    CategoryListView,
    )

app_name = 'product_list'


urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:pk>', product_list, name='product_category'),
    path('detail/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
    path('update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
]