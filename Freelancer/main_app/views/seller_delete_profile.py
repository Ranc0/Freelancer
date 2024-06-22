from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date

@api_view(['DELETE'])
def seller_delete_profile (request,id1,id2): 
    #data = request.data
    if Seller_Account.objects.filter(username = id1).exists():
        seller_account = Seller_Account.objects.get(username=id1)  
        profile = Profile.objects.filter(profile_seller_id = id2).get(seller_account = seller_account.pk)
        now = profile.serialize()
        profile.delete()
        now.update({'error': "no error found"})
        return Response (now)
    else :
        return Response ({'error': "no profile found to delete"})
