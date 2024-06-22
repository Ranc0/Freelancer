from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User, auth

@api_view(['POST'])
def customer_signin (request) :
    data = request.data
    if len(data['password']) == 0 or (len(data['username']) == 0 and len(data['email']) == 0) :
        return Response({ "error" : "some important values are not valid" })

    if User.objects.filter(username = data['username']).exists():
        user = User.objects.get(username = data['username'])
        customer_account = Customer_Account.objects.get(username = user)
        now = customer_account.serialize()
        now.update({ "id" : customer_account.username_id })
        return Response (now)
    else:
        return Response ({"error" : "user must sign up first"}) 