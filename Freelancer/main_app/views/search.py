from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
        
@api_view(['POST'])
def search(request):
    if request.method == 'POST':
        data = request.data
        b = False
        info = Profile.objects.all().order_by('-rate')
        account_query_set = Seller_Account.objects.all()
        for i,j in data.items():
            if i == "first_name":
                b = True
                account_query_set = account_query_set.filter(first_name__icontains = j)
            elif i == "second_name":
                b = True
                account_query_set = account_query_set.filter(second_name__icontains = j)
        if b == True:
            ids_array = account_query_set.only('id')
            info = info.filter(seller_account__in = ids_array)
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