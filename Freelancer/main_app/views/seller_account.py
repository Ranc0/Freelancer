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
def seller_account (request):
    if request.method == 'GET':
        user = request.user
        if Seller_Account.objects.filter(username = user).exists():
            info = Seller_Account.objects.get(username=user)
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
    