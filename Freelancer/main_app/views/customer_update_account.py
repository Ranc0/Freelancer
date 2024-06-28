from ..models import Seller_Account
from ..models import Customer_Account
from .. import validators as v
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

@api_view(['PUT'])
def customer_update_account (request) : 
    data = request.data
    user = request.user
    if not Customer_Account.objects.filter(username = user).exists():
        return Response({ "error" : "no customer with this username" })
    
    account =  Customer_Account.objects.get(username=user)
    
    if check_password('the default password', user.password):
        return Response ({"error" : "incorrect password"})
    
    # if (len(data["email"])==0 or len(data["first_name"])==0 or
    #     len(data["second_name"])==0 or len(data["phone_number"])==0):
    #      return Response ({"error" : "some values can't be empty"})
        

    info = account.serialize()
    for i,j in data.items() :
        if i == "username":
            continue
        if (i=="id") :
            return Response ({"error" : "you can't change account id , changes not saved"})
        if (i=='password'):
            continue
        elif (i=='new_password'):
            if (v.passwordChecker(j)):
                setattr(user , 'password' , j)
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
    user.save()

    info.update({"error" : "no error found"})
    return Response (info)
        
