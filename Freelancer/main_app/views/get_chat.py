from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Message , Chat 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_chat(request , username ):
    user1 = request.user
    chat = Chat.objects.filter( user = user1 ).filter( person2_username = username )
    serialized_messages = []
    if (not chat):
        return Response ({"messages":serialized_messages})
    chat = chat[0]
    messages = Message.objects.filter(chat = chat)
    for i in messages:
       serialized_messages.append(i.serialize())
    now = {}
    now.update({"messages":serialized_messages})

    return Response (now)
    