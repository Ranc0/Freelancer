from ..models import Seller_Account
from ..models import Customer_Account
from .. import validators as v
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def customer_update_account (request) : 
    data = request.data
    user = request.user
    user1 = authenticate(username = user.username, password=data['password'])
    if not user1:
        return Response({ "error" : "incorrect password, or user not found" })
    
    account =  Customer_Account.objects.filter(username=user)
    if not account.exists():
        return Response({ "error" : "no customer with this username" })

    account = account[0]
    info = account.serialize()
    arr = ['email','password','new_password','first_name','second_name',
    'country','bdate','phone_number','img']
    for i,j in data.items() :
        if i == "username":
            return Response({"error":"you can't change your username , changes not saved"})
        if (i=="id") :
            return Response ({"error":"you can't change account id , changes not saved"})
        if (i=='password'):
            continue
        elif (i=='new_password'):
            if (v.passwordChecker(j)):
                user.set_password(j)
                continue
            else :
                return Response ({"error" : "new password is not valid , length should be between 6 and 20"})
        elif (i=='email'):
            if (v.emailChecker(j) and Seller_Account.objects.filter(email=j).count()==0):
                info[i] = j
                setattr(account , i , j)
                user.email = j
                continue
            else :
                return Response ({"error" : "email not valid or used before"})
        elif (i=='phone_number'):
            if (v.phoneNumberChecker(j)):
                info[i] = j
                setattr(account , i , j)
                continue
            else :
                return Response ({"error" : "not a Syrian number"})    
        if i in arr:
            info[i] = j
            setattr(account , i , j)
        else:
            return Response({"error" : "some values are invalid to update"})
    account.save()
    user.save()

    info.update({"error" : "no error found"})
    return Response (info)
        
