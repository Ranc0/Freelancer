from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
        

@api_view(['GET'])
def customer_account(request,id):
    if request.method == 'GET':
        info = Customer_Account.objects.get(id=id)
        return Response(info.serialize())
    