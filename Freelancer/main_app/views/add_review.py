
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Deal_With , Review , Seller_Account , Profile , Customer_Account
from django.contrib.auth.models import User
from django.utils import timezone

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_review(request , username1 , id2 ):
    customer_user = request.user
    seller_query = User.objects.filter(username = username1)
    if not seller_query.exists() :
         return Response({"error": "no user with this username"})
    customer_account = Customer_Account.objects.filter(username = request.user)
    if not customer_account :
         return Response({"error": "you can add reviews from customer account only"})

    seller_user = seller_query[0]
    seller_account = Seller_Account.objects.get(username = seller_user)
    profile_query = Profile.objects.filter(seller_account = seller_account).filter(profile_seller_id=id2)
    if not profile_query.exists() :
         return Response({"error": "no profile with this id"})
    seller_profile = profile_query[0]
    
    deal_with = Deal_With.objects.filter(user = seller_user).filter(person2_id = customer_user.username).filter(profile = id2)
    if not deal_with.exists():
         return Response({"error":"no service to rate"})
    deal_with = deal_with.last

    if deal_with.is_accepted == 0:
         return Response({"error" : "you can't rate someone who didn't accept your offer"})
    
    if deal_with.end_time :
          end = deal_with.end_time
          today = timezone.now()
          msec = (today - end).seconds
          if msec > 604800000 and deal_with.is_active == 0:
               return Response({"error":"you can't rate this profile anymore"})
         
    data = request.data
    rate = 0
    comment = ""
    found_rate = 0
    for i, j in data.items():
         if i == 'rate' :
              j = int(j)
              j = min(j,5)
              rate += j 
              found_rate=1
          
         elif i == 'comment':
              comment += j
    if found_rate==0:
         return Response({"error":"rating must be added with at least 1 star"})
         
    review_query = Review.objects.filter(user = seller_user).filter(person2_id = customer_user.id).filter(profile = id2)
    if review_query.exists():
          review = review_query[0]
          old_rate = review.rate
          review.rate = rate
          review.comment = comment
          seller_profile.rate_sum -= old_rate
          seller_profile.rate_sum += rate
          seller_profile.rate = seller_profile.rate_sum / seller_profile.rate_cnt
          #return Response({"old_rate":old_rate})

          review.save()
    else:
         review = Review.objects.create(
              user = seller_user,
              person2_id = customer_user.username,
              profile = seller_profile.id,
              rate = rate,
              comment = comment
         )
         seller_profile.rate_sum += rate
         seller_profile.rate_cnt += 1
         seller_profile.rate = seller_profile.rate_sum / seller_profile.rate_cnt
    seller_profile.save()

    now = review.serialize()
    now.update({"error" : "no error"})
    return Response(now)
         
     
