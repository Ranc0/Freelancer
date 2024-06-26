from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Message , Chat
from django.contrib.auth.models import User

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request , id):
    user1 = request.user
    sender_id = user1.id
    text = request.data["message"]
    user2 = User.objects.filter(id = id)
    if (not user2):
         return Response({"error": "no user with this id"})
    
    user2 = user2[0]
    chat = Chat.objects.filter(user = user1).filter(person2_id = id)
    if not chat.exists():
         chat1 = Chat.objects.create(
              user = user1,
              person2_id = id,
         )
         chat2 = Chat.objects.create(
              user = user2,
              person2_id = sender_id,
              unread_cnt = 1
         )
    else:
         chat1 = chat[0]
         chat1.unread_cnt = 0
         chat2 = Chat.objects.filter(user = user2).get(person2_id = sender_id)
         chat2.unread_cnt += 1
         chat1.save()
         chat2.save()

    message1 = Message.objects.create(
        chat = chat1,
        message = text,
        sender = sender_id,
        reciever = id
    )
    message2 = Message.objects.create(
        chat = chat2,
        message = text,
        sender = sender_id,
        reciever = id
    )
    message1.save()
    message2.save()
    return Response({"error": "no error found"})
    
