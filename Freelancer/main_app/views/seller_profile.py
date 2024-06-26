from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Seller_Account , Profile 

@api_view(['GET'])    
@permission_classes([IsAuthenticated])
def seller_profile (request , id2):
    if request.method == 'GET':
        user = request.user
        seller_account = Seller_Account.objects.filter(username = user)
        seller_profile = Profile.objects.filter(profile_seller_id = id2).get(seller_account = seller_account.id)
        info = {}
        info.update({"user_id":user.id})
        info.update({"profile_id":id2})
        info .update(seller_profile.serialize())
        return Response(info)
