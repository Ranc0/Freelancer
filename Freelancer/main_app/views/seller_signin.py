from ..models import Seller_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def seller_signin (request) :
    #user = request.user
    data = request.data
    if len(data['password']) == 0 or (len(data['username']) == 0 ) :
        return Response({ "error" : "some important values are not valid" })
    user = User.objects.get(username = data['username'])
    
    seller_account =  Seller_Account.objects.filter(username = user)
    if (not seller_account.exists()):
        return Response ({"error" : "no such user as a seller , please sign up first"})
    
    if check_password('the default password', user.password):
        return Response ({"error" : "incorrect password"})
    if user.is_active == False:
        return Response ({"error" : "this account is banned , contact customer support if you think that was a mistake"})
        
    seller_account = seller_account[0]
    now = seller_account.serialize()
    now.update({ "id" : seller_account.username_id })
    now.update({ "error" : 'no error found'})
    now.update({'username': user.username})
    refresh = RefreshToken.for_user(user)
    now.update({'refresh': str(refresh)})
    now.update({'access': str(refresh.access_token)})
    return Response(now)
   