from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date

@api_view(['POST'])
def seller_create_profile (request,id): 
    data = request.data
    if Seller_Account.objects.filter(username = id).exists():
        seller_account_obj = Seller_Account.objects.get(username=id)       
        cnt = Profile.objects.filter(seller_account_id = seller_account_obj.pk).count()
        seller_profile = Profile.objects.create(
                    profile_seller_id = cnt+1,
                    language = data['language'],
                    work_group = data['work_group'],
                    bio = data['bio'],
                    provided_services = 0 ,
                    member_since = date.today(),
                    rate = 0,
                    seller_account = seller_account_obj,
        )
        now= seller_profile.serialize()
        now.update({'id': seller_profile.id})
        now.update({'error': "no error found"})
        return Response (now)
    else:
        return Response({ "error" : "no seller with this id" })
        
