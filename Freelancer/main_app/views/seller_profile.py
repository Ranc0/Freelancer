from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User 
from rest_framework.response import Response
from ..models import Seller_Account , Profile 

@api_view(['GET'])    
def seller_profile (request , username ,  id2):
    
        user = User.objects.filter(username = username)
        if (not user):
                return Response ({ "error":"no seller user with this username"})
        user = user[0]        
        seller_account = Seller_Account.objects.filter(username = user)
        if (not seller_account):
                return Response ({ "error":"no seller user with this username"})
        seller_account = seller_account[0]
        seller_profile = Profile.objects.filter(profile_seller_id = id2).filter(seller_account = seller_account.id)
        if not seller_profile.exists():
                return Response({"error":"there is no profile with this id for this seller"})
        seller_profile = seller_profile[0]

        info = seller_account.serialize()
        info.update({"profile_id":id2})
        info.update({"workgroup": seller_profile.work_group})
        info.update({"bio": seller_profile.bio})
        info.update({"provided_services": seller_profile.provided_services})
        info.update({"member_since" : seller_profile.member_since})
        info.update({"is_active" : seller_profile.is_active})
        info.update({"rate":seller_profile.rate})
        return Response(info)

