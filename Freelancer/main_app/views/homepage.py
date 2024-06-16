from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
        
@api_view(['GET','POST'])
def homepage(request):
    if request.method == 'GET':
        info = Profile.objects.all().order_by('-rate')
        profiles = []
        for profile in info:
            profiles.append({
                "profile_seller_id": profile.profile_seller_id,
                "language" : profile.language,
                "work_group" : profile.work_group,
                "bio" : profile.bio,
                "provided_services": profile.provided_services,
                "member_since" : profile.member_since,
                "rate" : profile.rate,
            })
        dectionary = {'profiles': profiles}
        return Response(dectionary)
    elif request.method == 'POST':
        data = request.data
        info = Profile.objects.all().order_by('-rate')
        for i,j in data.items():
            if i == "work_group":
                info = info.filter(work_group__in = j)
            elif i == "provided_services":
                info = info.filter(provided_services__gte = j)
            elif i == "rate":
                info = info.filter(rate__gte = j)
        profiles = []
        for profile in info:
            profiles.append({
                "profile_seller_id": profile.profile_seller_id,
                "language" : profile.language,
                "work_group" : profile.work_group,
                "bio" : profile.bio,
                "provided_services": profile.provided_services,
                "member_since" : profile.member_since,
                "rate" : profile.rate,
            })
        dectionary = {'profiles': profiles}
        return Response(dectionary)