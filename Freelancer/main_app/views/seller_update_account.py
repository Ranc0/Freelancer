from .. import validators as v
from ..models import Seller_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

@api_view(['PUT'])
def seller_update_account (request , id) : 
    data = request.data
    if not Seller_Account.objects.filter(username = id).exists():
        return Response({ "error" : "no seller with this id" })
    
    account =  Seller_Account.objects.get(username=id)
    user = User.objects.get(id=id)

    if check_password('the default password', user.password):
        return Response ({"error" : "incorrect password"})
            
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
   
        
