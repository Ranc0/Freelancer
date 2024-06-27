from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User 
from rest_framework.response import Response
from ..models import Seller_Account , Profile 

@api_view(['GET'])    
@permission_classes([IsAuthenticated])
def seller_profile (request , username , id2):
    
        user = User.objects.filter(username = username)
        if (not user):
                return Response ({ "error":"no user with this username"})
            
        seller_account = Seller_Account.objects.filter(username = user)
        if (not seller_account):
                return Response ({ "error":"no seller user with this username"})
        seller_account = seller_account[0]
        seller_profile = Profile.objects.filter(profile_seller_id = id2).get(seller_account = seller_account.id)

        info = {}

        info.update({"profile_id":id2})
        info.update({"username": username})
        info.update({"first_name": seller_account.first_name})
        info.update({"second_name": seller_account.second_name})
        rate = seller_profile.rate_sum  /  seller_profile.rate_cnt
        info.update({"rate":rate})
        info.update(seller_profile.serialize())
        return Response(info)
