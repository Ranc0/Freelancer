from ..models import Seller_Account
from .. import validators as v
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def seller_signup (request) : 
    data = request.data
    cnt = 0
    arr = ['username','email','password','password2','first_name','second_name',
    'country','bdate','phone_number','syriatel_cash','usdt','al_haram','id_picture' ,'id_picture2','img']
    dic = {}
    for i in arr:
        dic[i] = 0

    for i,j in data.items():
        if i in arr:
            dic[i] += 1
    
    for i,j in dic.items():
        if j > 1:
            return Response({ "error" : "some values are duplicate" })
        cnt += j
    if cnt != 15:
        return Response({ "error" : "some values are empty" })
    username = data['username']
    if len(username)>50:
         return Response({ "error" : "username max length is 50" })
    elif v.emailChecker(username)== 1:
        return Response({ "error" : "username can't be in email format" })
    email = data['email']
    password = data['password']
    password2 = data['password2']
    
    if (password==password2):
        if (Seller_Account.objects.filter(email=email).exists()):
            now = {'error': "this email is already used by a seller "}
            return Response (now)
        elif User.objects.filter(username=username).exists():
            now = {'error': "username already used"}
            return Response (now)
        else:
            if (v.emailChecker(data['email'])== 1 and v.passwordChecker(data['password'])== 1 and v.phoneNumberChecker(data['phone_number'])==1 ):
                    #cnt = User.objects.all().count()
                    user = User.objects.create_user(username = username , email = email , password = password)
                    seller_account = Seller_Account.objects.create (
                    username = user,
                    first_name= data['first_name'],
                    second_name= data['second_name'],
                    country= data['country'],
                    bdate= data['bdate'],
                    email= data['email'],
                    phone_number= data['phone_number'],
                    syriatel_cash= data['syriatel_cash'],
                    usdt= data['usdt'],
                    al_haram= data['al_haram'],
                    id_picture= data['id_picture'],
                    id_picture2= data['id_picture2']
                    )
                    if data['img'] != '':
                        seller_account.img = data['img']
                    seller_account.save()
                    now = seller_account.serialize()
                    now.update({'id': user.id})
                    now.update({'error': "no error found"})
                    now.update({'username': user.username})
                    user.save()
                    refresh = RefreshToken.for_user(user)
                    now.update({'refresh': str(refresh)})
                    now.update({'access': str(refresh.access_token)})
                    return Response (now)
            else:
                return Response ({"error" : "some important values are not valid"})
    else:
        now = {'error': "passwords are not the same"}
        return Response (now)
        
