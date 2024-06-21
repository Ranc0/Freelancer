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
    profile = Profile.objects.filter(profile_seller_id = id2).filter(seller_account = id1)
    if profile:
        profile = profile[0]
        now = profile.serialize()
        profile.delete()
        now.update({'error': "no error found"})
        return Response (now)
    else :
        return Response ({'error': "no profile found to delete"})
