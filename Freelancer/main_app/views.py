from django.shortcuts import render
from django.http import JsonResponse
from .models import Profile
from .models import Seller_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index (request) :
    return render (request , 'index.html')
@api_view(['GET'])
def profile (request , id) :
     if request.method == "GET": 
        info = Profile.objects.get(id = id)
        return Response(info.serialize())
@api_view(['GET'])     
def seller_account (request , id):
    if request.method == 'GET':
        info = Seller_Account.objects.get(id=id)
        seller_profiles_query_set = Profile.objects.filter(seller_account = info.pk)
        seller_profiles = []
        for pro in seller_profiles_query_set:
            seller_profiles.append({
                "profile_seller_id": pro.profile_seller_id,
                "language" : pro.language,
                "work_group" : pro.work_group,
                "bio" : pro.bio,
                "provided_services": pro.provided_services,
                "member_since" : pro.member_since,
                "rate" : pro.rate,
            })
        #print(seller_profiles)
        help = info.serialize()
        help.update({ "profiles":seller_profiles })
        #for key,value in help.items():
            #print(key + ": " + str(value))
        return Response(help)
@api_view(['GET'])    
def seller_profile (request , id , id1):
    if request.method == 'GET':
        info = Seller_Account.objects.get(id=id)
        seller_profile = Profile.objects.filter(seller_account = info.pk).get(id = id1)
        return Response(seller_profile.serialize())

   