from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from .. import validators as v
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date

@api_view(['POST'])
def customer_signup (request) : 
    data = request.data
    if (Customer_Account.objects.filter(email=data['email']).count()>0 ):
        return Response({"error" : "email is used before"})
    
    if (v.emailChecker(data['email'])== 1 and v.passwordChecker(data['password'])== 1
        and v.phoneNumberChecke(data['phone_number'])==1 ):
        customer_account = Customer_Account.objects.create (
                    first_name= data['first_name'],
                    second_name= data['second_name'],
                    password = data['password'],
                    country= data['country'],
                    bdate= data['bdate'],
                    email= data['email'],
                    phone_number= data['phone_number'],
                    member_since = date.today(),
            )
        now = customer_account.serialize()
        now.update({'id': customer_account.id})
        now.update({'error': "no error found"})
        return Response (now)
    else :
        return Response ({"error" : "some important values are not valid"})
    
        
