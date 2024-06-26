from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def seller_signin (request) :
    data = request.data
    if len(data['password']) == 0 or (len(data['username']) == 0 and len(data['email']) == 0) :
        return Response({ "error" : "some important values are not valid" })
    if (not User.objects.filter(username = data['username']).exists()):
          return Response ({"error" : "no such user"})
    user = User.objects.get(username = data['username'])
    if check_password('the default password', user.password):
        return Response ({"error" : "incorrect password"})
    
    if User.objects.filter(username = data['username']).exists():
        seller_account = Seller_Account.objects.filter(username = user)
        if (not seller_account):
             return Response({ "error" : "there is no seller with this username , are you sure you want to log in as a seller ?" })
        now = seller_account.serialize()
        now.update({ "id" : seller_account.username_id })
        now.update({ "error" : 'no error found'})
        refresh = RefreshToken.for_user(user)
        now.update({'refresh': str(refresh)})
        now.update({'access': str(refresh.access_token)})
        return Response(now)
    else:
        return Response ({"error" : "user must sign up first"}) 