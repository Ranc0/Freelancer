from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account , Profile
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
        
@api_view(['GET'])    
def seller_profile (request , id1 , id2):
    if request.method == 'GET':
        seller_profile = Profile.objects.filter(profile_seller_id = id2).get(seller_account = id1)
        info = {}
        info.update({"account_id":id1})
        info.update({"profile_id":id2})
        info .update(seller_profile.serialize())
        return Response(info)
