from rest_framework.decorators import api_view 
from rest_framework.response import Response
from ..models import  Review , Profile , Seller_Account
from django.contrib.auth.models import User

@api_view(['GET'])
def explore_reviews(request , seller_username , profile_id):
    seller_user = User.objects.filter(username = seller_username)
    if (not seller_user) :
         return Response({"error": "no seller with this username"})
    
    seller_user = seller_user[0]
    seller_account = Seller_Account.objects.get(username = seller_user)
    profile = Profile.objects.filter(seller_account = seller_account).filter(profile_seller_id =profile_id)
    if (not profile) :
         return Response({"error": "no profile with this id for this user"})

    reviews = Review.objects.filter(user = seller_user).filter(profile = profile_id)
    reviews_serialized = []
    for i in reviews:
        obj = i.serialize()
        customer_username = User.objects.get(username = i.person2_id)
        obj.update ({"customer_username" : customer_username.username})
        reviews_serialized.append(obj)
    return Response (reviews_serialized)
