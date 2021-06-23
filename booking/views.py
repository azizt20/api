from django.shortcuts import render
from .models import *
import datetime

# Create your views here.
def index(request):
    room = Room.objects.all()
    date_now = (datetime.datetime.now() - datetime.timedelta(days=10))
    qwerty = []
    for i in range(30) :
        qwerty.append((date_now + datetime.timedelta(days=i)).date())

    return render(request, 'index.html', {'r': room, 'd': qwerty})