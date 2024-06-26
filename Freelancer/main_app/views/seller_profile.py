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

@api_view(['GET'])    
@permission_classes([IsAuthenticated])
def seller_profile (request , id2):
    if request.method == 'GET':
        user = request.user
        seller_account = Seller_Account.objects.filter(username = user)
        seller_profile = Profile.objects.filter(profile_seller_id = id2).get(seller_account = seller_account.id)
        info = {}
        info.update({"user_id":user.id})
        info.update({"profile_id":id2})
        info .update(seller_profile.serialize())
        return Response(info)
