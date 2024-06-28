
from ..models import Customer_Account
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customer_account(request):
    user = request.user
    if request.method == 'GET':
        customer = Customer_Account.objects.filter(username = user)
        if customer.exists():
            customer = customer[0]
            now = customer.serialize()
            now.update({ "id" : customer.username_id })
            now.update({ "username" : user.username })
            return Response(now)
        else:
            return Response({ "error" : "no customer with this username" })
    