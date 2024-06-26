from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User, auth
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def customer_signin (request) :
    data = request.data
    if len(data['password']) == 0 or (len(data['username']) == 0 and len(data['email']) == 0) :
        return Response({ "error" : "some important values are not valid" })

    if User.objects.filter(username = data['username']).exists():
        user = User.objects.get(username = data['username'])
        customer_account = Customer_Account.objects.filter(username = user)
        if (not customer_account):
             return Response({ "error" : "there is no customer with this username , are you sure you want to log in as a customer ?" })
        customer_account = customer_account[0]
        now = customer_account.serialize()
        now.update({ "id" : customer_account.username_id })
        now.update({ "error" : "no error found"})
        refresh = RefreshToken.for_user(user)
        now.update({'refresh': str(refresh)})
        now.update({'access': str(refresh.access_token)})
        return Response (now)
    else:
        return Response ({"error" : "user must sign up first"}) 