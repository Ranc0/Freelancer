from .. import validators as v
from ..models import Seller_Account , Chat , Customer_Account , Message
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_chat (request , username) :
    user = request.user
    username_needed = username
    chats =  Chat.objects.filter(user = user)
    results = []
    for x in chats :
        if x.person2_username.startswith(username_needed):
           person2_username = User.objects.get(username = x.person2_username)
           serialized_chat = {}
           last_message = Message.objects.filter(chat = x).last()
           serialized_chat.update({ "image_message" : last_message.message })
           #serialized_chat.update({ "last_message" : x.message })
           if last_message.image_message:
            serialized_chat.update({ "image_message" : last_message.image_message })
           serialized_chat.update({ "username" :x.person2_username})
           serialized_chat.update({ "date" : last_message.date })
           serialized_chat.update({ "time" : last_message.time })
           serialized_chat.update({ "sender" : last_message.sender })
           serialized_chat.update({ "reciever" : last_message.reciever })
           if Seller_Account.objects.filter(username = person2_username).exists():
            img = Seller_Account.objects.get(username = person2_username).img
           elif Customer_Account.objects.filter(username = person2_username).exists():
            img = Customer_Account.objects.get(username =person2_username).img
           serialized_chat.update({ "img" : img })
           results.append(serialized_chat)
    return Response ({'result' : results})