from django.shortcuts import render
from django.http import JsonResponse
from .models import Profile
from .models import Seller_Account
from .models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index (request) :
    routes = [
        {
            "endpoint" : 'account/seller/id',
            "method" : 'GET',
            "description" : "returns info of the seller account with this id"
        }
        ,
        {
            "endpoint" : 'account/customer/id',
            "method" : 'GET',
            "description" : "returns info of the customer account with this id"
        }
        ,
        {
            "endpoint" : 'account/seller/account_id/profile/profile_id',
            "method" : 'GET',
            "description" : "returns the profile with (profile_id) of the seller account with (account_id)"

        },
            ]
    return Response(routes)

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

@api_view(['GET'])
def customer_account(request,id):
    if request.method == 'GET':
        info = Customer_Account.objects.get(id=id)
        return Response(info.serialize())
    
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
        groups = request.data
        info = Profile.objects.filter(work_group__in = groups['work_groups']).order_by('-rate')
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