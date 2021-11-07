from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessageSerializer
from .models import Message


@api_view(['GET'])
def home(request):
    api_urls = {
        'List': '/list-messages',
        'Detail View': '/message-detail/<str:pk>/',
        'Create': '/message-create/',
        'Update': '/message-update/<str:pk>/',
        'Delete': '/message-delete/<str:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def messageList(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def messageDetail(request, pk):
    messages = Message.objects.get(id=pk)
    serializer = MessageSerializer(messages, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def messageCreate(request):
    serializer = MessageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PATCH'])
def messageUpdate(request, pk):
    message = Message.objects.get(id=pk)
    serializer = MessageSerializer(instance=message, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def messageDelete(request, pk):
    message = Message.objects.get(id=pk)
    message.delete()

    return Response("The item is successfully deleted")
