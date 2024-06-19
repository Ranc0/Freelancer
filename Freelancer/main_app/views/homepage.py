from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
        
@api_view(['GET'])
def homepage(request):
    if request.method == 'GET':
        info = Profile.objects.all().order_by('-rate')
        profiles = []
        for profile in info:
            profiles.append({
                "profile_id": profile.profile_seller_id,
                "account_id": profile.seller_account.pk,
                "language" : profile.language,
                "work_group" : profile.work_group,
                "bio" : profile.bio,
                "provided_services": profile.provided_services,
                "member_since" : profile.member_since,
                "rate" : profile.rate,
            })
        dectionary = {'profiles': profiles}
        return Response(dectionary)