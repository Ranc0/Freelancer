from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('account/seller/<int:id>' , views.seller_account , name='seller_account'),
    path('account/seller/<int:id>/profile/<int:id1>' , views.seller_profile , name='seller_profile'),
    path('account/customer/<int:id>', views.customer_account),
    path('homepage', views.homepage)

]