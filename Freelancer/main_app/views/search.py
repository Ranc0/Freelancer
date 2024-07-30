from ..models import Profile
from ..models import Seller_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
        
@api_view(['POST'])
def search(request):
    if request.method == 'POST':
        data = request.data
        b = False
        info = Profile.objects.all().order_by('-rate')
        account_query_set = Seller_Account.objects.all()
        for i,j in data.items():
            if i == "username":
                b = True
                user = User.objects.filter(username = j)
                if not user:
                    list = []
                    return Response({'profiles':list})
                user = user[0]
                account_query_set = account_query_set.filter(username = user )
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
            elif i == "active":
                info = info.filter(is_active = j)
        profiles = []
        for profile in info:
            seller_obj = Seller_Account.objects.get(id =profile.seller_account.pk)
            username = seller_obj.username.username
            img = seller_obj.img
            profiles.append({
                "username": username,
                "first_name": seller_obj.first_name,
                "last_name": seller_obj.second_name,
                "profile_id": profile.profile_seller_id,
                "img" : img,
                "language" : profile.language,
                "work_group" : profile.work_group,
                "bio" : profile.bio,
                "provided_services": profile.provided_services,
                "member_since" : profile.member_since,
                "rate" : profile.rate,
                "is_active" : profile.is_active
            })
        dectionary = {'profiles': profiles}
        return Response(dectionary)