from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
        
@api_view(['GET'])    
def seller_profile (request , id , id1):
    if request.method == 'GET':
        info = Seller_Account.objects.get(id=id)
        seller_profile = Profile.objects.filter(seller_account = info.pk).get(id = id1)
        return Response(seller_profile.serialize())
