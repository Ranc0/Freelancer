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
    cnt = Profile.objects.filter(seller_account = id).count()
    seller_account_obj = Seller_Account.objects.get(id=id)
    seller_profile = Profile.objects.create(
                profile_seller_id = cnt,
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
        
