from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from retros_api.models import Student


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    """

    new_user = User.objects.create_user(
        username=request.data['username'],
        email=request.data['email'],
        password=request.data['password'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name']
    )

    if request.data.get('github_url'):
        Student.objects.create(
            github_url=request.data['github_url'],
            cohort_id=request.data['cohort_id'],
            user=new_user
        )

    token = Token.objects.create(user=new_user)
    data = {'token': token.key}
    return Response(data)
