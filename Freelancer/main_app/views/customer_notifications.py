from rest_framework.decorators import api_view 
from rest_framework.response import Response
from ..models import  Customer_Account , Deal_With
from django.contrib.auth.models import User

@api_view(['GET'])
def customer_notifications(request):
    customer = request.user
    if not Customer_Account.objects.filter(username = customer):
        return Response({"error" : "no customer with this username"})
    deals = Deal_With.objects.filter(person2_id = customer.username).filter(is_accepted = 1)
    info = []
    for deal in deals:
        info.append(deal.serialize())
    now = {}
    now.update({"notifications":info})
    return Response(now)
