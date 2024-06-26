from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Message , Chat
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_chat(request , id ):
    user1 = request.user
    chat = Chat.objects.filter( user = user1 ).get( person2_id = id )
    messages = Message.objects.filter(chat = chat)
    serialized_messages = []
    for i in messages:
       serialized_messages.append(i.serialize())
    now = {}
    now.update({"messages":serialized_messages})

    return Response (now)
    