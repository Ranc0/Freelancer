from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from main_app.models import Deal_With , Customer_Account,Seller_Account,Chat,Message,Review,Profile
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['GET'])
def index (request) :
    routes = [
        { 
            "note": "you need to be a staff member to be able to access these routes , so your ((access)) token must be included in the request header "
        },

        {
            "endpoint" : 'staff/check_service/customer_username/seller_username/profile_id',
            "method" : 'GET',
            "description" : "returns ((result)) which is a message answering if there is a service between these two persons"
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

    user = User.objects.filter(Q(username = sent_username) and Q(is_staff = True))
    if (not user) :
         return Response ({"result" : "this username doesn't exist as a staff member"})
    user = user[0]
    if check_password('the default password', user.password):
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

    if (not Customer_Account.objects.filter(username =customer_username)):
         return Response({"result": "no customer with this username is found"})
    if (not Seller_Account.objects.filter(username =seller_username)):
         return Response({"result": "no seller with this username is found"})
    obj = Deal_With.objects.filter(Q(user = User.objects.get(username = seller_username).id)and Q(person2_id = User.objects.get(username = customer_username.id))
                                    and  Q(profile = profile_id)  and  Q(is_accepted = True))
    res = ""
    if (obj) :
        res = "YES ! there is a service between this profile and this customer"
    else :
         res = "YES ! there is a service between this profile and this customer"
    
    return Response({"result": res})

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_chat(request , username1 , username2  ):
    user1 = User.objects.filter(username = username1)
    user2 = User.objects.filter(username = username2)
    if (not user1):
        return Response({"result": "this username" +username1 + "doesn't exist"})
    if (not user2):
        return Response({"result": "this username" +username2 + "doesn't exist"})

    chat = Chat.objects.filter( user = user1 ).get( person2_id = user2.id )
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
    
    profile_id = obj[0].profile
    seller_id = obj[0].user
    profile = Profile.filter.get(Q(seller_account = seller_id) and Q( profile_seller_id= profile_id))
    rate_sum = profile.rate_sum-obj.rate
    rate_cnt = profile.rate_cnt - 1

    profile.rate_sum = rate_sum
    profile.rate_cmt = rate_cnt
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






