from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def token(request , user ):
    refresh = RefreshToken.for_user(user)
    return Response( {
      'refresh': str(refresh),
        'access': str(refresh.access_token),
    })