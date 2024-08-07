from ..models import Profile
from ..models import Seller_Account
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import date

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def seller_create_profile (request): 
    data = request.data
    user = request.user
    if Seller_Account.objects.filter(username = user).exists():
        seller_account_obj = Seller_Account.objects.get(username=user)   
        arr = ["Interior Designer" ,"Designer" ,"Doctor" ,
               "IT Engineer" , "Architecture Engineer" ,"Lawyer" ,"Translator" ,"Teacher"] 
        desired_workgroup = data['work_group']
        if (desired_workgroup not in arr) :
            return Response({ "error" : "this workgroup is not available in our app yet" })
        
        already = Profile.objects.filter(seller_account_id = seller_account_obj.id)
        arr = []
        for i in range(0,len(already)):
            arr.append(already[i].work_group)
        if (desired_workgroup in arr):
            return Response({ "error" : "you already have a profile for this workgroup" })


        cnt = Profile.objects.filter(seller_account_id = seller_account_obj.id).count()
        seller_profile = Profile.objects.create(
                    profile_seller_id = cnt+1,
                    language = data['language'],
                    work_group = data['work_group'],
                    bio = data['bio'],
                    provided_services = 0 ,
                    member_since = date.today(),
                    rate_sum = 0,
                    rate_cnt = 0 ,
                    seller_account = seller_account_obj,
        )
        now= seller_profile.serialize()
        now.update({'id': seller_profile.profile_seller_id})
        now.update({"img":seller_account_obj.img})
        now.update({'first_name': seller_account_obj.first_name})
        now.update({'last_name': seller_account_obj.second_name})
      
        now.update({'error': "no error found"})
        return Response (now)
    else:
        return Response({ "error" : "only a seller can make a profile" })
        
