from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import date
from ..models import Deal_With , Review , Seller_Account , Profile 
from django.contrib.auth.models import User, auth
from django.db.models import Q
import datetime

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def end_service(request, id , id2):
    seller_user = request.user
    customer_user = User.objects.filter(id = id)
    if not customer_user.exists():
        return Response({"error": "no user with this id"})
    
    customer_user = customer_user[0]
    service = Deal_With.objects.filter(user = seller_user).filter(person2_id = customer_user.id).filter(profile = id2)
    if not service.exists():
        return Response({"error":"there is no such service to end"})
    
    service = service[0]
    if service.is_accepted == 0:
        return Response({"error":"accept the service before end it "})
    
    if service.is_active == 0:
        return Response({"error":"service already had ended"})
    
    service.is_active = 0 
    service.end_time = datetime.datetime.now().date()
    service.save()

    now = service.serialize()
    now.update({"error":"service deleted, no errors"})
    return Response(now)
    