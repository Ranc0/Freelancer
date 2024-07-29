from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Deal_With , Profile 
from django.contrib.auth.models import User
from django.db.models import Q

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def service_requests (request):
    requests = Deal_With.objects.filter(user = request.user and Q(is_accepted = False) )
    serialized_requests= []
    for i in requests :
        profile_object = Profile.objects.get(id = i.profile)
        customer_object = User.objects.get(username = i.person2_id)
        service_id = i.id
        workgroup = profile_object.work_group
        customer_username = customer_object.username
        time = i.send_time
        date = i.send_date
        obj = {}
        obj.update({"profile_id" : i.profile })
        obj.update({"workgroup" : workgroup })
        obj.update({"customer_username" : customer_username })
        obj.update({"customer_id" : customer_object.id })
        obj.update({"request_time" : time })
        obj.update({"request_date" : date })
        serialized_requests.append(obj)
    return Response(serialized_requests)