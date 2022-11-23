from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse

from .models import Users, Repositories, Documents
from .serializers import UsersSerializers, RepositoriesSerializers, DocumentsSerializers


@api_view(['GET'])
def getUsers(request):
    user = Users.objects.all()
    serializer = UsersSerializers(user, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def saveUsers(request):
    data = JSONParser().parse(request)
    user = UsersSerializers(data=data)

    if user.is_valid():
        user.save()
        return JsonResponse(user.data, status=status.HTTP_201_CREATED)
    return JsonResponse(user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetRepositories(request):
    repositorie = Repositories.objects.all()
    serializer = RepositoriesSerializers(repositorie, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def SaveRepositories(request):
    data = JSONParser().parse(request)
    RepoSerializer = RepositoriesSerializers(data=data)
    if RepoSerializer.is_valid():
        RepoSerializer.save()
        return JsonResponse(RepoSerializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(RepoSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def SaveDocument(request):

    data = JSONParser().parse(request)
    DocumentSerializer = DocumentsSerializers(data=data)

    if DocumentSerializer.is_valid():
        DocumentSerializer.save()
        return JsonResponse(DocumentSerializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
