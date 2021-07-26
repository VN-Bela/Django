from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('products/',views.product),
    path('customer/<str:pk_test>',views.customer),
] 