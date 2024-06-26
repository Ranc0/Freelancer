from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import date
from ..models import Deal_With , Review , Seller_Account , Profile
from django.contrib.auth.models import User, auth
from django.db.models import Q
import datetime

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_review(request , id1 , id2 ):
    customer_user = request.user
    seller_query = User.objects.filter(id = id1)
    if not seller_query.exists() :
         return Response({"error": "no user with this id"})
    customer_account = customer_account.objects.filter(user = request.user)
    if not customer_account :
         return Response({"error": "you can add reviews from customer account only"})

    seller_user = seller_query[0]
    seller_account = Seller_Account.objects.get(username = seller_user)
    profile_query = Profile.objects.filter(seller_account = seller_account).filter(profile_seller_id=id2)
    if not profile_query.exists() :
         return Response({"error": "no profile with this id"})
    seller_profile = profile_query[0]
    
    deal_with = Deal_With.objects.filter(user = seller_user).filter(person2_id = customer_user.id).filter(profile = id2)
    if not deal_with.exists():
         return Response({"error":"no service to rate"})
    deal_with = deal_with[0]

    if deal_with.is_accepted == 0:
         return Response({"error" : "you can't rate someone who didn't accept your offer"})
    
    if deal_with.end_time :
          end = datetime.strptime(deal_with.end_time, "%Y-%m-%d")
          today = datetime.strptime(datetime.datetime.now().date(), "%Y-%m-%d")
          days = (today - end).days
          if days > 7 and deal_with.is_active == 0:
               return Response({"error":"rating timeout"})
         
    data = request.data
    rate = 0
    comment = ""
    found_rate = 0
    for i, j in data.items():
         if i == 'rate' and j>0:
              rate += j 
              found_rate=1
          
         elif i == 'comment':
              comment += j
    if(found_rate==0):
         return Response({"error":"rating must be added with at least 1 star"})
         
    review_query = Review.objects.filter(user = seller_user).filter(person2_id = customer_user.id)
    if review_query.exists():
          review = review_query[0]
          old_rate = review.rate
          review.rate = rate
          if comment != "" :
               review.comment = comment
          seller_profile.rate -= old_rate
          seller_profile.rate += rate

          review.save()
    else:
         review = Review.objects.create(
              user = seller_user,
              person2_id = customer_user.id,
              profile = seller_profile.id,
              rate = rate,
              comment = comment
         )
         seller_profile.rate += rate
    seller_profile.save()

    now = review.serialize()
    now.update({"error" : "no error"})
    return Response(now)
         
     
