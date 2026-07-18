"""
URL configuration for ecomsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path("<int:id>/",views.detail, name="detail"),
    path("cart/add/<int:id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart, name="cart"),
    path("cart/remove/<int:id>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart/increase/<int:id>/", views.increase_quantity, name="increase_quantity"),
    path("cart/decrease/<int:id>/", views.decrease_quantity, name="decrease_quantity"),
]
