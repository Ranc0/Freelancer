from django.urls import path 
from . import views

urlpatterns = [
    path('' ,views.index ),
    path('check_service/<str:customer_username>/<str:seller_username>/<int:profile_id>',views.check_service ),
    path('get_chat/<str:username1>/<str:username2>' ,views.get_chat),
    path('get_review/<int:id>' ,views.get_review ),
    path('delete_review/<int:id>' ,views.delete_review ),
    path('ban/<str:username>' ,views.ban_user),
    path('unban/<str:username>' ,views.unban_user),
    path('signin' ,views.sign_in),
    path('get_seller_info/<str:username>', views.get_seller_info)
   
    ]