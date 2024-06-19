from django.urls import path 
from .views import customer_account
from .views import homepage
from .views import index
from .views import seller_account
from .views import seller_profile
from .views import search
from .views import seller_signup
from .views import seller_update_account

urlpatterns = [
    path('',index, name='index'),
    path('account/seller/<int:id>' , seller_account , name='seller_account'),
    path('account/seller/<int:id>/profile/<int:id1>' ,seller_profile , name='seller_profile'),
    path('account/customer/<int:id>', customer_account),
    path('homepage', homepage),
    path('signup/seller', seller_signup),
    path('search', search),
     path('update/seller/<int:id>', seller_update_account),

]