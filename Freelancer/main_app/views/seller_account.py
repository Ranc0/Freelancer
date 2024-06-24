from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])     
def seller_account (request , id):
    if request.method == 'GET':
        if Seller_Account.objects.filter(username = id).exists():
            info = Seller_Account.objects.get(username=id)
            seller_profiles_query_set = Profile.objects.filter(seller_account = info.id)
            seller_profiles = []
            for pro in seller_profiles_query_set:
                seller_profiles.append({
                    "profile_id": pro.profile_seller_id,
                    "language" : pro.language,
                    "work_group" : pro.work_group,
                    "bio" : pro.bio,
                    "provided_services": pro.provided_services,
                    "member_since" : pro.member_since,
                    "rate" : pro.rate,
                })
            now = info.serialize()
            now.update({ "profiles" : seller_profiles })
            return Response(now)
        else:
            return Response({ "error" : "no seller with this id" })
    