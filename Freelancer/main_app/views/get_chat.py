from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import date
from ..models import Message
from django.contrib.auth.models import User, auth
from django.db.models import Q
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_chat(request , id ):
    user1 = request.user
    messages = Message.objects.filter(user = user1 and  Q(sender=id) | Q(reciever=id)) 
    serialized_messages = []
    for i in messages:
       serialized_messages.append(i.serialize())
    now = {}
    now.update({"messages":serialized_messages})

    return Response (now)
    