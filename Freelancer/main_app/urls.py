from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('profile/<int:id>',views.profile, name='profile'),
    path('account/seller/<int:id>' , views.seller_account , name='seller_account'),
    path('account/seller/<int:id>/profile/<int:id1>' , views.seller_profile , name='seller_profile')

]