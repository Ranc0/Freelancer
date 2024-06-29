from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Deal_With
from django.contrib.auth.models import User
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_service(requset , customer_username , seller_username , profile_id):
    customer_user = User.objects.get(username = customer_username) 
    seller_user = User.objects.get(username = seller_username)

    #if (requset.user != customer_user and requset.user != seller_user):
        #return Response ({"error" : "you can't delete someone else's service offers"})
    
    service_object = Deal_With.objects.filter(user = seller_user).filter(person2_id = customer_user.id).filter(profile = profile_id)
    if (not service_object) :
        return Response ({"error" : "such service doesn't exist"})
    if service_object[0].is_accepted :
        return Response ({"error" : "you can't delete a service request if it has been accepted"})
    
    service_object = service_object[0]
    service_object.delete()
    return Response ({"error" : "service deleted, no error found"})