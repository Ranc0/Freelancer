from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Seller_Account , Profile 

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
            now.update({"img" : info.img})
            profiles_sorted = sorted(seller_profiles, key=lambda x: x["rate"], reverse=True)
            now.update({ "profiles" : profiles_sorted })
            return Response(now)
        else:
            return Response({ "error" : "no seller with this id" })
    