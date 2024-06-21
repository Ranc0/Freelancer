from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from .. import validators as v
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['PUT'])
def customer_update_account (request , id) : 
    data = request.data
    account =  Customer_Account.objects.get(id=id)
    oldpass = account.password
    sentpass = data['password']

    if (oldpass!=sentpass):
        return Response ({"error" : "incorrect password"})
    
    # if (len(data["email"])==0 or len(data["first_name"])==0 or
    #     len(data["second_name"])==0 or len(data["phone_number"])==0):
    #      return Response ({"error" : "some values can't be empty"})
        

    info = account.serialize()
    for i,j in data.items() :
        if (i=="id") :
            return Response ({"error" : "you can't change account id , changes not saved"})
        if (i=='password'):
            continue
        elif (i=='new_password'):
            if (v.passwordChecker(j)):
                setattr(account , 'password' , j)
                continue
            else :
                return Response ({"error" : "new password is not valid , length should be between 6 and 20"})
        elif (i=='email'):
            if (v.emailChecker(j) and Seller_Account.objects.filter(email=j).count()==0):
                info[i] = j
                setattr(account , i , j)
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
            
        info[i] = j
        setattr(account , i , j)
    account.save()

    info.update({"error" : "no error found"})
    return Response (info)
        
