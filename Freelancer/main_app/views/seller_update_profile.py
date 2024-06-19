from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['PUT'])
def seller_update_profile (request, id1, id2) : 
    data = request.data
    account = Seller_Account.objects.get(id = id1)
    profile = Profile.objects.filter(profile_seller_id = id2).get(seller_account = id1)
    oldpass = account.password
    sentpass = data['password']

    if (oldpass!=sentpass):
        return Response ({"error" : "incorrect password"})
    
    if len(data["language"])==0 or len(data["work_group"])==0 :
         return Response ({"error" : "some values can't be empty"})
        

    info = profile.serialize()
    for i,j in data.items() :
        if i == "password":
            continue
        info[i] = j

    info.update({"error" : "no error found"})
    return Response (info)
   
        
