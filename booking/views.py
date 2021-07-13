from django.shortcuts import render
from .models import RoomType, Room, Order
from rest_framework import generics
from rest_framework.response import Response
from .serializers import DateModelSerializer, RoomTypeModelSerializer, RoomModelSerializer, OrderModelSerializer, \
    Order1ModelSerializer, Room1ModelSerializer, RoomType1ModelSerializer
import datetime

# Create your views here.

date_now = (datetime.datetime.now() - datetime.timedelta(days=10))
qwerty = []
for i in range(30):
    qwerty.append((date_now + datetime.timedelta(days=i)).date())


def index(request):
    room = Room.objects.all()
    return render(request, 'index.html', {'r': room, 'd': qwerty})

class RoomTypeList(generics.ListCreateAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeModelSerializer


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


class RoomType1List(generics.ListCreateAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomType1ModelSerializer


class Room1List(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = Room1ModelSerializer


class Order1List(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = Order1ModelSerializer

