from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Deal_With , Profile , Seller_Account , Customer_Account
from django.contrib.auth.models import User
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def active_services (request):
    active = []
    if (Customer_Account.objects.filter( username = request.user)):
          active = Deal_With.objects.filter(person2_id=request.user.username).filter(is_accepted = True).filter(is_active = 1)
    else :
         active = Deal_With.objects.filter(user = request.user).filter(is_accepted = True).filter(is_active = 1)
    
    serialized_active_services= []
    for i in active :
        profile_object = Profile.objects.get(id = i.profile)
        customer_object = User.objects.get(username = i.person2_id)
        seller_object = User.objects.get(username = i.user)
        service_id = i.id
        workgroup = profile_object.work_group
        customer_username = customer_object.username
        seller_username = seller_object.username
        time = i.send_time
        date = i.send_date
        obj = {}
        obj.update({"profile_id" : i.profile })
        obj.update({"workgroup" : workgroup })
        obj.update({"customer_username" : customer_username })
        obj.update({"seller_username" : seller_username })
        obj.update({"request_time" : time })
        obj.update({"request_date" : date })
        obj.update({"accept_time" : i.accept_time})
        serialized_active_services.append(obj)
    return Response(serialized_active_services)
