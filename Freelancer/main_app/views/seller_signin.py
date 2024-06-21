from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['POST'])
def seller_signin (request) :
    data = request.data
    if (len(data["email"])>0 and len(data['password']) >0 ):
        seller_account = Seller_Account.objects.filter(email = data['email']).filter(password = data['password'])
        if not seller_account:
            return Response ({"error" : "incorrect credentials"})
        else:
            seller_account = seller_account[0]
            return Response (seller_account.serialize())
    else:
        return Response ({"error" : "some values are empty"}) 