from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def models_documentation(request):
    routes = [
        { 
            "name": "Seller account",
            "fields": [
                "username: Anas1",
                "first_name: Anas",
                "second_name: DA",
                "country: Syria",
                "bdate: 2002-1-15",
                "email: Anas2@gmail.com",
                "phone_number: 0999222222",
                "password: 123123",
                "password2: 123123",
                "syriatel_cash: True",
                "usdt: True",
                "al_haram: True",
                "id_picture: heheboy"
            ]
        },
        {
            "name": "Profile",
            "fields" :[
                "language: Arabic",
                "work_group: IT",
                "bio: Mobile Application Developper (IOS and Android)",
                "provided_services: 12",
                "member_since: 2020-12-12",
                "rate = 3.1"
            ]
        },
        {
            "name" : "Customer account",
            "fields":[
                "username: Rani1",
                "first_name: Rani",
                "second_name: Ali",
                "country: Syria",
                "bdate: 2002-8-15",
                "email: Rani@gmail.com",
                "phone_number: 0988888888",
                "member_since: 2017-1-17"
            ]
        }
    ]
    return Response(routes)