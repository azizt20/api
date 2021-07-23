from django.shortcuts import render
from .models import RoomType, Room, Order, Menu
from rest_framework import generics
from rest_framework.response import Response
from .serializers import DateModelSerializer, RoomTypeModelSerializer, RoomModelSerializer, OrderModelSerializer, \
    Order1ModelSerializer, Room1ModelSerializer, RoomType1ModelSerializer
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

# Create your views here.

date_now = (datetime.datetime.now() - datetime.timedelta(days=10))
qwerty = []
for i in range(30):
    qwerty.append((date_now + datetime.timedelta(days=i)).date())


def home(request):
    # room = Room.objects.all()
    return render(request, 'home.html')
    # return render(request, 'index.html', {'r': room, 'd': qwerty})

def room(request):
    return render(request, 'room.html')

def booking(request):
    return render(request, 'booking.html')

def relax(request):
    return render(request, 'relax.html')

def kitchen(request):
    menu = Menu.objects.all()
    return render(request, 'kitchen.html', {'m': menu})


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

