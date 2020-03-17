"""LearnDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# ECOMMERCE URLS.PY

from . import views
from django.urls import path,include
from rest_framework import routers
from .views import ProductViewSet,ReviewViewSet

router = routers.DefaultRouter()
router.register('' , ProductViewSet)
router1 = routers.DefaultRouter()
router1.register('' , ReviewViewSet)


urlpatterns = [
    path('', views.homepage , name = 'homepage'),
    path('/productview/<int:myid>' , views.productview , name = 'productview'),
    path('/checkout' , views.checkout , name = 'checkout'),
    path('/contact' , views.contact , name = 'contact'),
    path('/cart' , views.cart , name = 'cart'),
    path('/search' , views.search , name = 'search'),
    path('/products/<str:value>' , views.products , name = 'products'),
    path('/cart/api/' , include(router.urls)),
    path('/review/api/' , include(router1.urls)),
]
