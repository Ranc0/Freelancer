from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import date
from ..models import Message , Chat
from django.contrib.auth.models import User, auth
from django.db.models import Q

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def explore_chats(request):
    user1 = request.user
    chats = Chat.objects.filter( user = user1 )
    unread_chats = 0 
    
    serialized_chats = []
    for i in chats:
       serialized_chat = i.serialize()
       if serialized_chat['unread_cnt']:
           unread_chats += 1
       last_message = Message.objects.filter(chat = i).last()
       last_message = last_message.serialize()
       serialized_chat.update({ "last_message" : last_message })
       serialized_chats.append(serialized_chat)
    now = {}
    now.update({"unread_chats" : unread_chats})
    now.update({"chats" : serialized_chats})

    return Response (now)
    