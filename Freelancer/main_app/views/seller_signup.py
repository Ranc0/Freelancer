from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def seller_signup (request) : 
    data = request.data
    if (len(data["email"])>0 and len(data["first_name"])>0 and
    len(data["second_name"])>0 and len(data["phone_number"])>0 and
    len(data['password']) >0 ):
        seller_account = Seller_Account.objects.create (
                    first_name= data['first_name'],
                    second_name= data['second_name'],
                    password = data['password'],
                    country= data['country'],
                    bdate= data['bdate'],
                    email= data['email'],
                    phone_number= data['phone_number'],
                    syriatel_cash= data['syriatel_cash'],
                    usdt= data['usdt'],
                    al_haram= data['al_haram'],
                    id_picture= data['id_picture']
            )
        now= seller_account.serialize()
        now.update({'id': seller_account.id})
        now.update({'error': "no error found"})
        return Response (now)
    else:
        return Response ({"error" : "some values are empty"})
        
