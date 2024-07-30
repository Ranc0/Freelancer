from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Deal_With , Seller_Account , Profile
from django.contrib.auth.models import User
import datetime

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def end_service(request, username , id2):
    seller_user = request.user
    customer_user = User.objects.filter(username = username)
    if not customer_user.exists():
        return Response({"error": "no user with this username"})
    
    if (not Seller_Account.objects.filter(username = request.user)):
         return Response({"error": " you must be a seller to end your services"})
    
    customer_user = customer_user[0]
    service = Deal_With.objects.filter(user = seller_user).filter(person2_id = customer_user.username).filter(profile = id2)
    if not service.exists():
        return Response({"error":"there is no such service to end"})
    
    service = service.last()
    if service.is_accepted == 0:
        return Response({"error":"accept the service before end it "})
    
    if service.is_active == 0:
        return Response({"error":"service already had ended"})
    
    seller_account = Seller_Account.objects.get(username = request.user)
    
    profile = Profile.objects.filter(seller_account = seller_account ).get(profile_seller_id = id2)
    profile.provided_services += 1
    profile.save()
    service.is_active = 0 
    service.end_time = datetime.datetime.now().date()
    service.save()

    now = service.serialize()
    now.update({"error":"service ended, no errors"})
    return Response(now)
    