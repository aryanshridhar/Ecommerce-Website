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

from django.urls import path
from .views import Productlistview , Productview , Createapiview , ProductUpdateview , ProductDeleteview

urlpatterns = [
    path('/productlist',Productlistview.as_view()),
    path('/product/<int:pk>',Productview.as_view()),
    path('/createproduct' , Createapiview.as_view()),
    path('/product/<int:pk>/update' , ProductUpdateview.as_view()),
    path('/product/<int:pk>/delete' , ProductDeleteview.as_view()),

] 
