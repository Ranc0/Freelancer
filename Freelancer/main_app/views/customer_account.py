
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

@api_view(['GET'])
def customer_account(request,id):
    if request.method == 'GET':
        if Customer_Account.objects.filter(username = id).exists():
            username = User.objects.get(username = id).username
            info = Customer_Account.objects.get(username = id)
            now = info.serialize()
            now.update({ "id" : info.username_id })
            now.update({ "username" : username })
            return Response(now)
        else:
            return Response({ "error" : "no customer with this id" })
    