from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

@api_view(['POST'])
def customer_signin (request) :
        data = request.data
        if len(data['password']) == 0 or (len(data['username']) == 0) :
            return Response({ "error" : "some important values are not valid" })
        customer_account = None
        user = User.objects.filter(username = data['username'])
        if (user) :
            customer_account =  Customer_Account.objects.filter(username = user[0])
            if (not customer_account.exists()):
                return Response ({"error" : "no such user as a customer , please sign up first"})
        else :
            return Response ({"error" : "no such user as a customer , please sign up first"})

        user = user[0]

        if check_password('the default password', user.password):
            return Response ({"error" : "incorrect password"})
        if user.is_active == False:
            return Response ({"error" : "this account is banned , contact customer support if you think that was a mistake"})
        
        customer_account = customer_account[0]
        now = customer_account.serialize()
        now.update({ "id" : customer_account.username_id })
        now.update({ "error" : "no error found"})
        refresh = RefreshToken.for_user(user)
        now.update({'refresh': str(refresh)})
        now.update({'access': str(refresh.access_token)})
        return Response (now)
    