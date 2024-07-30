from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import  Seller_Account , Profile 


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def seller_update_profile (request, id2) : 
    data = request.data
    seller_user = request.user
    seller_account = Seller_Account.objects.filter(username = seller_user)
    if not seller_account.exists():
        return Response({ "error" : "no seller with this id" })
    
    seller_account = seller_account[0]
    profile = Profile.objects.filter(profile_seller_id = id2).filter(seller_account = seller_account.pk)
    if not profile.exists():
        return Response({ "error" : "no profile with this id for this seller" })

    profile = profile[0]
    arr = ["bio" , "language"]

    info = profile.serialize()
    for i,j in data.items() :
        if (i=="id") :
            return Response ({"error" : "you can't change profile id , changes not saved"})
        if i in arr:
            info[i] = j
            setattr(profile , i , j)
        else:
            return Response({"error" : "some values are invalid to update"})
    profile.save()

    info.update({"error" : "no error found"})
    return Response (info)
   
        
