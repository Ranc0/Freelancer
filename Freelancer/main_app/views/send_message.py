from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import date
from ..models import Message
from django.contrib.auth.models import User, auth
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
    message = Message.objects.create(
        user = user1,
        message = text,
        sender = sender_id,
        reciever = id
    )
    message2 = Message.objects.create(
        user = user2,
        message = text,
        sender = sender_id,
        reciever = id
    )
    message.save()
    message2.save()
    return Response({"error": "added successfully"})
    
