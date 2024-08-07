from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from main_app.models import Deal_With , Customer_Account,Seller_Account,Chat,Message,Review,Profile
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


@api_view(['GET'])
def index (request) :
    routes = [
        { 
            "note": "you need to be a staff member to be able to access these routes , so your ((access)) token must be included in the request header "
        },

        {
            "endpoint" : 'staff/check_service/customer_username/seller_username/profile_id',
            "method" : 'GET',
            "description" : "returns ((result)) which is a message answering if there is a service between these two persons , and ((state)) which is either active or finished"
        },
        {
            "endpoint" : 'staff/get_chat/username1/username2',
            "method" : 'GET',
            "description" : "returns ((result)) which is the messages between these two users"
        },
        {
            "endpoint" : 'staff/get_review/id',
            "method" : 'GET',
            "description" : "returns ((result)) which is the review with the sent id"
        },
        {
            "endpoint" : 'staff/delete_review/id',
            "method" : 'POST',
            "description" : "deletes the review with the sent id , returns ((result)) as well"
        },
        {
            "endpoint" : 'staff/ban/username',
            "method" : 'POST',
            "description" : "bans the user with this username , returns ((result)) as well"
        },
        {
            "endpoint" : 'staff/unban/username',
            "method" : 'POST',
            "description" : "unbans the user with this username , returns ((result)) as well"
        },
        {
            "endpoint" : 'staff/get_seller_info/username',
            "method" : 'PUT',
            "description" : "get the basic info of a seller like (first_name , last_name , phone_number , email , img , id_picture , username)"
        },
    ]
    return Response (routes)


@api_view(['POST'])
def sign_in (request):
    data = request.data
    cnt = 0 
    for i,j in data.items():
        if i=="username":
            cnt+=1
        if i=="password":
            cnt+=1
    
    if cnt!=2:
        return Response ({"result" : "please provide a username and a password"})

    sent_pass = request.data["password"]
    sent_username = request.data["username"]

    user = User.objects.filter(username = sent_username).filter(is_staff = True)
    if (not user) :
         return Response ({"result" : "this username doesn't exist as a staff member"})
    user = user[0]
    user_authenticated = authenticate(username=user.username, password=sent_pass)
    if not user_authenticated :
        return Response ({"result" : "incorrect password"})

    now = {}
    refresh = RefreshToken.for_user(user)
    now.update({'refresh': str(refresh)})
    now.update({'access': str(refresh.access_token)})
    now.update ({"error" : "signed in successfully"})
    return Response (now)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def check_service(request , customer_username , seller_username , profile_id ):

    customer_username = User.objects.filter(username = customer_username)
    seller_username = User.objects.filter(username = seller_username)
    if not customer_username:
        return Response({"error" : "there is no customer with this username"})
    if not seller_username:
        return Response({"error" : "there is no seller with this username"})
    customer_username = customer_username[0]
    seller_username = seller_username[0]

    if (not Customer_Account.objects.filter(username = customer_username)):
         return Response({"result": "no customer with this username is found"})
    if (not Seller_Account.objects.filter(username = seller_username)):
         return Response({"result": "no seller with this username is found"})
    
    seller_account = Seller_Account.objects.get(username = seller_username)
    if not Profile.objects.filter(seller_account = seller_account).filter(profile_seller_id = profile_id).exists():
        return Response({"error":"there is no profile with this id for this seller"})
    obj = obj = Deal_With.objects.filter(user = seller_username).filter(person2_id = customer_username.id).filter(profile = profile_id).filter(is_accepted = True)
    res = ""
    if (obj) :
        res = "YES ! there is a service between this profile and this customer"
    else :
         res = "No ! there is no service between this profile and this customer"
    obj = obj.last
    state=""
    if (obj.is_active==1) :
        state = "active"
    else :
        state = "finished"
    return Response({"result": res , "state": state})

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_chat(request , username1 , username2  ):
    user1 = User.objects.filter(username = username1)
    user2 = User.objects.filter(username = username2)
    if (not user1):
        return Response({"result": "this username" +username1 + "doesn't exist"})
    if (not user2):
        return Response({"result": "this username" +username2 + "doesn't exist"})
    user1 = user1[0]
    user2 = user2[0]
    if not Seller_Account.objects.filter(username = user1).exists() or not Customer_Account.objects.filter(username = user1).exists():
        return Response({"error" : "first user is not a seller nor a customer"})
    
    if not Seller_Account.objects.filter(username = user2).exists() or not Customer_Account.objects.filter(username = user2).exists():
        return Response({"error" : "second user is not a seller nor a customer"})

    chat = Chat.objects.filter( user = user1 ).get( person2_username = user2.username )
    messages = Message.objects.filter(chat = chat)
    serialized_messages = []
    for i in messages:
       serialized_messages.append(i.serialize())
    now = {}
    now.update({"result":serialized_messages})
    return Response (now)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_review(request , id ):
    obj = Review.objects.filter(id = id)
    if (not obj):
          return Response({"result": "a review with this id doesn't exist"})
    obj = obj[0].serialize()
    return Response(obj)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_review(request , id ):
    obj = Review.objects.filter(id = id)
    if (not obj):
          return Response({"result": "a review with this id doesn't exist"})
    obj = obj[0]
    profile_id = obj.profile
    seller_user = obj.user
    seller_account = Seller_Account.objects.get(username = seller_user)
    profile = Profile.objects.filter(seller_account = seller_account).filter( profile_seller_id = profile_id)
    profile = profile[0]
    profile.rate_sum -= obj.rate
    profile.rate_cnt -= 1
    if profile.rate_cnt :
        profile.rate = profile.rate_sum / profile.rate_cnt
    else:
        profile.rate = 0

    profile.save()
    obj.delete()
    return Response({"result" : "deleted successfully"})

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def ban_user(request , username ):
    user = User.objects.filter(username = username)
    if not user:
        return Response({"result" : "a user with this username doesn't exist"})
    user = user[0]
    user.is_active = False
    user.save()

    return Response ({"result" : "user is banned and can't log in with this username again"})

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def unban_user(request , username ):
    user = User.objects.filter(username = username)
    if not user:
        return Response({"result" : "a user with this username doesn't exist"})
    user = user[0]
    user.is_active = True
    user.save()

    return Response ({"result" : "user is unbanned and can log in now"})


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def get_seller_info(request , username):
    user = User.objects.filter(username = username)
    user = user[0]
    seller = Seller_Account.objects.filter(username = user)
    if not seller.exists():
        return Response({"error":"there is no such seller"})
    info = seller[0]
    
    now = info.serialize()
    now.update({"img" : info.img})
    now.update({"id_picture" : info.id_picture})
    now.update({"id_picture2" : info.id_picture2})
    now.update({"first_name" : info.first_name})
    now.update({"last_name" : info.second_name})
    now.update({"username" : username})
    now.update({"email" : info.email})
    now.update({"phone_number" : info.phone_number})
   
    return Response(now)



