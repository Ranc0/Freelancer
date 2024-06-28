from ..models import Profile
from ..models import Seller_Account
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import date

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def seller_create_profile (request): 
    data = request.data
    user = request.user
    if Seller_Account.objects.filter(username = user).exists():
        seller_account_obj = Seller_Account.objects.get(username=user)       
        cnt = Profile.objects.filter(seller_account_id = seller_account_obj.id).count()
        seller_profile = Profile.objects.create(
                    profile_seller_id = cnt+1,
                    language = data['language'],
                    work_group = data['work_group'],
                    bio = data['bio'],
                    provided_services = 0 ,
                    member_since = date.today(),
                    rate_sum = 0,
                    rate_cnt = 0 ,
                    seller_account = seller_account_obj,
        )
        now= seller_profile.serialize()
        now.update({'id': seller_profile.profile_seller_id})
        now.update({"img":seller_account_obj.img})
        now.update({'error': "no error found"})
        return Response (now)
    else:
        return Response({ "error" : "no seller with this id" })
        
