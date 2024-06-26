from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Deal_With 
from django.db.models import Q
import datetime
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def accept_service (requset , customer_id , profile_id):
    service_object = Deal_With.objects.filter(user = requset.user and Q(person2_id = customer_id) 
                                              and Q(profile = profile_id))
    if (not service_object) :
        return Response ({"error" : "such service doesn't exist"})
    service_object = service_object[0]
    service_object.is_accepted = True
    service_object.is_active = True
    service_object.accept_time = datetime.datetime.now().date()
    service_object.save()
    return Response ({"error" : "no error found" , "accept_time" :service_object.accept_time ,
                      "is_accepted" : service_object.is_accepted  })