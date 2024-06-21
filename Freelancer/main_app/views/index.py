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
         {
            "endpoint" : 'homepage',
            "method" : 'GET',
            "description" : "returns a list of profiles from top rated to lowest "

        },
        {
            "endpoint" : 'search',
            "method" : 'post',
            "description" : "you send a json file with the attributes you want to filter on , you can filter on (first_name, second_name, work_group, provided_services, rate)"

        },
         {
            "endpoint" : "signup/seller",
            "method" : 'post',
            "description" : "you send a json file with all info of the new seller account , you recieve a json file with the attributes you sent , an ((id)) attribute which is the id of the account you made and an ((error)) attribute which is value is 'no error found' if everything was fine"

        },
         {
            "endpoint" : "update/seller/account_id",
            "method" : 'put',
            "description" : "you send a json file with all info of the seller account that you want to update including ((password)) , if passwords match you get the the new info with ((error))='no error found' , if you want to change password you send ((new_password)) attribute as well"

        },
        {
            "endpoint" : "update/seller/account_id/profile/profile_id",
            "method" : 'put',
            "description" : "you send a json file with all info of the seller account's proifle that you want to update , you recieve a json file with new data"
        },
        {
            "endpoint" : "signin/seller",
            "method" : 'post',
            "description" : "you send a json file with email and password of the seller account, if correct you reciece this account info with ((error))=='no error found' "
        },
        {
            "endpoint" : "delete/seller/account_id/profile/profile_id",
            "method" : 'delete',
            "description" : "you just request the url and the profile is deleted "
        },
        {
            "endpoint" : "create/seller/account_id/profile",
            "method" : 'post',
            "description" : "you send a json file with all info of the profile you want to make for this account , you receive the info back and the profile id "
        },
         {
            "endpoint" : "update/customer/account_id",
            "method" : 'put',
            "description" : "you send a json file with all info of the customer account that you want to update including ((password)) , if passwords match you get the the new info with ((error))='no error found' , if you want to change password you send ((new_password)) attribute as well"
        },
        {
            "endpoint" : "signup/customer",
            "method" : 'post',
            "description" : "you send a json file with all info of the new customer account , you recieve a json file with the attributes you sent , an ((id)) attribute which is the id of the account you made and an ((error)) attribute which is value is 'no error found' if everything was fine"
        }
        ,
        {
            "endpoint" : "signin/customer",
            "method" : 'post',
            "description" : "you send a json file with email and password of the customer account, if correct you reciece this account info with ((error))=='no error found' "
        }
            ]
    return Response(routes)