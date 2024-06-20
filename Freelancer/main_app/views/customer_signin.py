from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['POST'])
def customer_signin (request) :
    data = request.data
    if len(data["email"])>0 and len(data['password'])>0:
        customer_account = Customer_Account.objects.filter(email = data['email']).get(password = data['password'])
        return Response (customer_account.serialize())
    else:
        return Response ({"error" : "some values are empty"}) 