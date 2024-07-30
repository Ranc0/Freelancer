from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Seller_Account , Profile 

@api_view(['GET'])    
@permission_classes([IsAuthenticated])
def resume_profile (request , id1):
    user = request.user
    seller_account = Seller_Account.objects.filter(username = user)
    if not seller_account.exists():
        return Response({"error" : "current user is not a seller"})
    
    seller_account = seller_account[0]
    profile = Profile.objects.filter(seller_account = seller_account).filter(profile_seller_id = id1)
    if not profile.exists():
        return Response({"error" : "no profile with this id for this seller"})
    
    profile = profile[0]
    if profile.is_active == True :
        return Response({"error" : "profile already worked"})
    profile.is_active = True
    profile.save()
    return Response({"error" : "no errors, profile resumed"})