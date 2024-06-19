from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['PUT'])
def seller_update_account (request , id) : 
    data = request.data
    account =  Seller_Account.objects.get(id=id)
    oldpass =account.password
    sentpass = data['password']

    if (oldpass!=sentpass):
        return Response ({"error" : "incorrect password"})
    
    if (len(data["email"])==0 or len(data["first_name"])==0 or
    len(data["second_name"])==0 or len(data["phone_number"])==0):
         return Response ({"error" : "some values can't be empty"})
        

    info = account.serialize()
    for i,j in data.items() :
        info[i] = j

    info.update({"error" : "no error found"})
    return Response (info)
   
        
