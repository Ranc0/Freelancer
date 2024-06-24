from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from .. import validators as v
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date
from django.contrib.auth.models import User, auth
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def customer_signup (request) : 
    data = request.data
    b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = b9 = 0
    for i, j in data.items():
        if i == 'username': b1 = 1
        elif i == 'email' : b2 = 1
        elif i == 'password' : b3 = 1
        elif i == 'password2' : b4 = 1
        elif i == 'first_name' : b5 = 1
        elif i == 'second_name' : b6 = 1
        elif i == 'country' : b7 = 1
        elif i == 'bdate' : b8 = 1
        elif i == 'phone_number' : b9 = 1
                  
    if not b1 or not b2 or not b3 or not b4 or not b5 or not b6 or not b7 or not b8 or not b9 :
        return Response({ "error" : "some values are empty" })
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
            if(v.emailChecker(data['email'])== 1 and v.passwordChecker(data['password'])== 1 and v.phoneNumberChecker(data['phone_number'])==1 ):
                    user = User.objects.create_user(username = username , email = email , password = password)
                    customer_account = Customer_Account.objects.create (
                    username = user,
                    first_name= data['first_name'],
                    second_name= data['second_name'],
                    country= data['country'],
                    bdate= data['bdate'],
                    email= data['email'],
                    phone_number= data['phone_number'],
                    member_since = date.today(),
                )
                    now = customer_account.serialize()
                    now.update({'id': user.id})
                    now.update({'error': "no error found"})
                    user.save()
                    refresh = RefreshToken.for_user(user)
                    now.update({'refresh': str(refresh)})
                    now.update({'access': str(refresh.access_token)})
                    return Response (now)
            else :
                return Response ({"error" : "some important values are not valid"})
    else:
        now = {'error': "passwords are not the same"}
        return Response (now)
    
        
