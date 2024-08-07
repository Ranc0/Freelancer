from .. import validators as v
from ..models import Seller_Account , Chat , Customer_Account
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def search_chat (request , username) :
    user = request.user
    data = request.data
    username_needed = username
    chats =  Chat.objects.filter(user = user)
    results = []
    for x in chats :
        if x.person2_username.startswith(username_needed):
           serialized_chat = {}
           serialized_chat.update({ "last_message" : x.message })
           if x.image_message:
             serialized_chat.update({ "image_message" : x.image_message })
           serialized_chat.update({ "username" :x.person2_username})
           serialized_chat.update({ "date" : x.date })
           serialized_chat.update({ "time" : x.time })
           serialized_chat.update({ "sender" : x.sender })
           serialized_chat.update({ "reciever" : x.reciever })
           if Seller_Account.objects.filter(username = x.person2_username).exists():
            img = Seller_Account.objects.get(username = x.person2_username).img
           elif Customer_Account.objects.filter(username = x.person2_username).exists():
            img = Customer_Account.objects.get(username =x.person2_username).img
           serialized_chat.update({ "img" : img })
           results.append(serialized_chat)
    return Response ({'result' : results})