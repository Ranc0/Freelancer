from .. import validators as v
from ..models import Seller_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
@api_view(['PUT'])
def seller_update_account (request) : 
    data = request.data
    user = request.user
    user = authenticate(username = user.username, password=data['password'])
    if not user:
        return Response ({"error" : "incorrect password, or user not found"})
    
    account = Seller_Account.objects.filter(username = user)
    if not account.exists():
        return Response({ "error" : "no seller with this username" })
    
    account = account[0]
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
   
        
