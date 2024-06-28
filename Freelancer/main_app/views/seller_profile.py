from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User 
from rest_framework.response import Response
from ..models import Seller_Account , Profile 

@api_view(['GET'])    
@permission_classes([IsAuthenticated])
def seller_profile (request , id2):
    
        user = request.user
        seller_account = Seller_Account.objects.filter(username = user)
        if (not seller_account):
                return Response ({ "error":"no seller user with this username"})
        seller_account = seller_account[0]
        seller_profile = Profile.objects.filter(profile_seller_id = id2).filter(seller_account = seller_account.id)
        if not seller_profile.exists():
                return Response({"error":"there is no profile with this id for this seller"})

        info = {}

        info.update({"username": user.username})
        info.update({"first_name": seller_account.first_name})
        info.update({"second_name": seller_account.second_name})
        info.update({"profile_id":id2})
        if seller_profile.rate_cnt:
                rate = seller_profile.rate_sum  /  seller_profile.rate_cnt
        else:
                rate = 0
        info.update({"rate":rate})
        info.update(seller_profile.serialize())
        return Response(info)

