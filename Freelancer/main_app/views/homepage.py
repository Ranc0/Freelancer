from ..models import Profile ,Seller_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
        
@api_view(['GET'])
def homepage(request):
    if request.method == 'GET':
        info = Profile.objects.filter(is_active = True)
        profiles = []
        for profile in info:
            seller_obj = Seller_Account.objects.get(id = profile.seller_account.pk)
            username = seller_obj.username.username
            img = seller_obj.img

            profiles.append({
                "profile_id": profile.profile_seller_id,
                "username": username,
                "first_name": seller_obj.first_name,
                "second_name": seller_obj.second_name,
                "img" : img,
                "language" : profile.language,
                "work_group" : profile.work_group,
                "bio" : profile.bio,
                "provided_services": profile.provided_services,
                "member_since" : profile.member_since,
                "rate" : profile.rate ,
                "is_active" : profile.is_active
            })
        profiles_sorted = sorted(profiles, key=lambda x: x["rate"], reverse=True)
        dectionary = {'profiles': profiles_sorted}
        return Response(dectionary)