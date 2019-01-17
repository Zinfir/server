"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from product_list.api.categories import CategoryViewSet
from product_detail.api.products import ProductViewSet, ProductListLeftViewSet, ProductListRightViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)

default_router = [
    path('categories/', include('product_list.endpoints.categories'))
] 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('product_list/', include('product_list.urls.product_list')),
    path('product_detail/', include('product_detail.urls.product_detail')),
    path('contacts/', include('contacts.urls')),
    path('accounts/', include('accounts.urls')),
    path('default_api/', include(default_router)),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
