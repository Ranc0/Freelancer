from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import date
from ..models import Deal_With , Review , Seller_Account , Profile 
from django.contrib.auth.models import User, auth
from django.db.models import Q
import datetime

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def seller_update_profile (request, id1, id2) : 
    data = request.data
    if not Seller_Account.objects.filter(username = id1).exists():
        return Response({ "error" : "no seller with this id" })
    seller_account = Seller_Account.objects.get(username=id1) 
    if not Profile.objects.filter(profile_seller_id = id2).filter(seller_account = seller_account.pk).exists():
        return Response({ "error" : "no profile with this id" })


    profile = Profile.objects.filter(profile_seller_id = id2).get(seller_account = seller_account.pk)

    info = profile.serialize()
    for i,j in data.items() :
        if (i=="id") :
            return Response ({"error" : "you can't change profile id , changes not saved"})
        info[i] = j
        setattr(profile , i , j)
    profile.save()

    info.update({"error" : "no error found"})
    return Response (info)
   
        
