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
def explore_reviews(request , seller_id , profile_id):
    seller_user = User.objects.filter(id = seller_id)
    if (not seller_user) :
         return Response({"error": "no seller with this id"})
    
    profile = Profile.objects.filter(Seller_Account = seller_id and Q(id =profile_id) )
    if (not profile) :
         return Response({"error": "no profile with this id for this user"})

    reviews = Review.objects.filter(user = seller_id and Q(profile = profile_id))
    reviews_serialized = []
    for i in reviews:
        obj = i.serialize()
        customer_username = User.objects.get(id = i.person2_id)
        obj.update ({"customer_username" : customer_username})
        reviews_serialized.append(obj)
    return Response (reviews_serialized)
