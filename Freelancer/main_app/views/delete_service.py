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
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_service(requset , customer_id , seller_id , profile_id):
    customer_user = User.objects.filter(id = customer_id) 
    seller_user = User.objects.filter(id = seller_id)

    if (requset.user != customer_user and requset.user != seller_user):
        return Response ({"error" : "you can't delete someone else's service offers"})
    
    service_object = Deal_With.objects.filter(user = seller_id and Q(person2_id = customer_id) 
                                              and Q(profile = profile_id))
    if (not service_object) :
        return Response ({"error" : "such service doesn't exist"})
    if (service_object[0].is_acceptd) :
        return Response ({"error" : "you can't delete a service request if it has been accepted"})
    
    service_object = service_object[0]
    service_object.delete()
    return Response ({"error" : "no error found"})