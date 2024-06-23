from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from .. import validators as v
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User, auth
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def seller_signup (request) : 
    data = request.data
    username = data['username']
    email = data['email']
    password = data['password']
    password2 = data['password2']
    
    if (password==password2):
        if (User.objects.filter(email=email).exists()):
            now = {'error': "email is already used"}
            return Response (now)
        elif User.objects.filter(username=username).exists():
            now = {'error': "username already used"}
            return Response (now)
        else:
            if (v.emailChecker(data['email'])== 1 and v.passwordChecker(data['password'])== 1 and v.phoneNumberChecker(data['phone_number'])==1 ):
                    #cnt = User.objects.all().count()
                    user = User.objects.create_user(username = username , email = email , password = password)
                    seller_account = Seller_Account.objects.create (
                    username = user,
                    first_name= data['first_name'],
                    second_name= data['second_name'],
                    country= data['country'],
                    bdate= data['bdate'],
                    email= data['email'],
                    phone_number= data['phone_number'],
                    syriatel_cash= data['syriatel_cash'],
                    usdt= data['usdt'],
                    al_haram= data['al_haram'],
                    id_picture= data['id_picture']
                    )
                    now = seller_account.serialize()
                    now.update({'id': user.id})
                    now.update({'error': "no error found"})
                    user.save()
                    refresh = RefreshToken.for_user(user)
                    now.update({'refresh': str(refresh)})
                    now.update({'access': str(refresh.access_token)})
                    return Response (now)
            else:
                return Response ({"error" : "some important values are not valid"})
    else:
        now = {'error': "passwords are not the same"}
        return Response (now)
        
