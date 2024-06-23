from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User, auth

@api_view(['GET'])
def customer_account(request,id):
    if request.method == 'GET':
        if Customer_Account.objects.filter(username = id).exists():
            info = Customer_Account.objects.get(username = id)
            now = info.serialize()
            now.update({ "id" : info.username_id })
            return Response(now)
        else:
            return Response({ "error" : "no customer with this id" })
    