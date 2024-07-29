from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Deal_With , Seller_Account , Profile , Customer_Account 
from django.contrib.auth.models import User
import datetime

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def start_service(request, username , id2):
    customer_user = request.user
    seller_user = User.objects.filter(username = username)
    if not seller_user.exists():
        return Response({"error": "no user with this id"})
    
    if (not Customer_Account.objects.filter(username = request.user)):
         return Response({"error": " you must be a customer to start a service"})
    if (not Seller_Account.objects.filter(username = username)):
         return Response({"error": " no seller with this username"})
    
    seller_user = seller_user[0]
    seller_account = Seller_Account.objects.get(username = seller_user)
    profile_query = Profile.objects.filter(seller_account = seller_account).filter(profile_seller_id=id2)

    if not profile_query.exists() :
         return Response({"error": "no profile with this id"})
    
    seller_profile = profile_query[0]
    if (seller_profile.is_active==False):
          return Response({"error": "can't start a service with a profile that is not activated"})
    
    serv = Deal_With.objects.filter(user = seller_user).filter(person2_id = customer_user.username).filter(profile=id2)
    if serv.exists():
          serv = serv.last
          if serv.is_accepted == 0:
            return Response({"error": "a request to this profile already exisits , you can either delete it or wait till accepted"})
          
        
    service = Deal_With.objects.create(
        user = seller_user,
        profile = seller_profile.profile_seller_id,
        person2_id = customer_user.username,
    )
    now = service.serialize()
    now.update({"error":"no error"})
    return Response(now)

