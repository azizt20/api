from django.shortcuts import render
from django.views.generic import View
import datetime

from booking.forms import BookingForm
from booking.models import RoomType
from booking.models import Room
from booking.models import Order



class Dashboard(View):
    def get(self, request):
        datatime_list = []
        asd = datetime.datetime.now() - datetime.timedelta(10)
        for i in range(30):
            i = i + 1
            datatime_list.append(asd + datetime.timedelta(i))

        data = {}
        skip = set()

        for order in Order.objects.select_related('room').all():
            key = "{}_{:%Y-%m-%d}".format(order.room.room_type, order.start_date)
            data[key] = order

            current = (order.start_date + datetime.timedelta(days=1))
            while current < order.finish_date:
                key = "{}_{:%Y-%m-%d}".format(order.room.room_type, current)
                skip.add(key)
                current = (current + datetime.timedelta(days=1))

        context = {
            'form': BookingForm(),
            'current_Date': datetime.date.today(),
            'month': datatime_list,
            'data': data,
            'skip': skip,
            'types': RoomType.objects.all(),
            'rooms': Room.objects.all()
        }
        return render(request, 'dashboard.html', context)