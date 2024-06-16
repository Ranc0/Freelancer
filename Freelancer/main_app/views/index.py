from django.shortcuts import render
from django.http import JsonResponse
from ..models import Profile
from ..models import Seller_Account
from ..models import Customer_Account
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index (request) :
    routes = [
        {
            "endpoint" : 'account/seller/id',
            "method" : 'GET',
            "description" : "returns info of the seller account with this id"
        }
        ,
        {
            "endpoint" : 'account/customer/id',
            "method" : 'GET',
            "description" : "returns info of the customer account with this id"
        }
        ,
        {
            "endpoint" : 'account/seller/account_id/profile/profile_id',
            "method" : 'GET',
            "description" : "returns the profile with (profile_id) of the seller account with (account_id)"

        },
            ]
    return Response(routes)