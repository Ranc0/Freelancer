from django.urls import path 
from .views import customer_account
from .views import homepage
from .views import index
from .views import seller_account
from .views import seller_profile
from .views import search
from .views import seller_signup
from .views import seller_update_account
from .views import seller_signin
from .views import seller_update_profile
from .views import seller_create_profile
from .views import seller_delete_profile
from .views import customer_signup
from .views import customer_signin
from .views import customer_update_account
from .views import forms
from .views import send_message
from .views import get_chat
from .views import explore_chats
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',index, name='index'),
    path('account/seller/<int:id>' , seller_account , name='seller_account'),
    path('account/seller/<int:id1>/profile/<int:id2>' ,seller_profile , name='seller_profile'),
    path('account/customer/<int:id>', customer_account),
    path('homepage', homepage),
    path('signup/seller', seller_signup),
    path('search', search),
    path('update/seller/<int:id>', seller_update_account),
    path('signin/seller', seller_signin),
    path('update/seller/<int:id1>/profile/<int:id2>', seller_update_profile),
    path('create/seller/<int:id>/profile', seller_create_profile),
    path('delete/seller/<int:id1>/profile/<int:id2>', seller_delete_profile),
    path('signup/customer', customer_signup),
    path('signin/customer', customer_signin),
    path('update/customer/<int:id>', customer_update_account),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('forms', forms),
    path('chat/send/<int:id>', send_message),
    path('chat/<int:id>', get_chat),
    path('chats' , explore_chats),

]