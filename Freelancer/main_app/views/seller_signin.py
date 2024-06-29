from ..models import Seller_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def seller_signin (request) :
    #user = request.user
    data = request.data
    if len(data['password']) == 0 or (len(data['username']) == 0 ) :
        return Response({ "error" : "some important values are not valid" })
    user = authenticate(username=data['username'], password=data['password'])
    
    seller_account =  Seller_Account.objects.filter(username = user)
    if (not seller_account.exists()):
        return Response ({"error" : "no such user as a seller , please sign up first"})
    
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
   