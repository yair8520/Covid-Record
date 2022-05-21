from rest_framework.decorators import api_view
from rest_framework.response import Response

from records.models import User
from records.seirializers import UserSerializer


@api_view(['post'])
def addUser(request):
    seirializer = UserSerializer(data=request.data)
    if seirializer.is_valid():
        seirializer.save()
        return Response(data="Report added successfully")

    return Response(data="Failed to Add Report")


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    usersList = UserSerializer(users, many=True)
    return Response(usersList.data)
