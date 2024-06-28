from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Message , Chat , Seller_Account , Customer_Account
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def explore_chats(request):
    user1 = request.user
    chats = Chat.objects.filter( user = user1 ).order_by('-time')
    unread_chats = 0 
    
    serialized_chats = []
    for i in chats:
       serialized_chat = i.serialize()
       if serialized_chat['unread_cnt']:
           unread_chats += 1
       last_message = Message.objects.filter(chat = i).last()
       user2 = User.objects.get(username = i.person2_username)
       if Seller_Account.objects.filter(username = user2).exists():
        img = Seller_Account.objects.get(username = user2).img
       elif Customer_Account.objects.filter(username = user2).exists():
        img = Customer_Account.objects.get(username = user2).img

       serialized_chat.update({ "last_message" : last_message.message })
       if last_message.image_message:
          serialized_chat.update({ "image_message" : last_message.image_message })
       serialized_chat.update({ "username" : i.person2_username})
       serialized_chat.update({ "date" : last_message.date })
       serialized_chat.update({ "time" : last_message.time })
       serialized_chat.update({ "sender" : last_message.sender })
       serialized_chat.update({ "reciever" : last_message.reciever })
       serialized_chat.update({ "img" : img })
       
       serialized_chats.append(serialized_chat)
    now = {}
    now.update({"unread_chats" : unread_chats})
    now.update({"chats" : serialized_chats})

    return Response (now)
    