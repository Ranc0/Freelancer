from ..models import Profile
from ..models import Seller_Account
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import date

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def available_profiles (request):
     user = request.user
        
     seller_account_obj = Seller_Account.objects.get(username=user)   
     arr = ["Interior Designer" ,"Designer" ,"Doctor" ,
               "IT Engineer" , "Architecture Engineer" ,"Lawyer" ,"Translator" ,"Teacher"]   
     already = Profile.objects.filter(seller_account_id = seller_account_obj.id) 
     arr1 = []
     for i in range(0,len(already)):
          arr1.append(already[i].work_group)
     available = []
     for i in arr :
          if i not in arr1:
               available.append(i)
     return Response ({"result" : available})