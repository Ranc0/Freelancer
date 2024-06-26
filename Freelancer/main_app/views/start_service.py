from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import date
from ..models import Deal_With , Review , Seller_Account , Profile 
from django.contrib.auth.models import User, auth
from django.db.models import Q

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_service(request, id , id2):
    customer_user = request.user
    seller_user = User.objects.filter(id = id)
    if not seller_user.exists():
        return Response({"error": "no user with this id"})
    
    seller_user = seller_user[0]
    seller_account = Seller_Account.objects.get(username = seller_user)
    profile_query = Profile.objects.filter(seller_account = seller_account).filter(profile_seller_id=id2)

    if not profile_query.exists() :
         return Response({"error": "no profile with this id"})
    
    seller_profile = profile_query[0]
    
    service = Deal_With.objects.create(
        user = seller_user,
        profile = seller_profile.profile_seller_id,
        person2_id = customer_user.id,
    )
    now = service.serialize()
    now.update({"error":"no error"})
    return Response(now)

