from django.shortcuts import render, redirect
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
        print("------------")
        for i in datatime_list:
            print(i.weekday())
        print('asdasdasd')
        print(datetime.date.today().weekday())
        print('--------------')
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

    def post(self, request):
        room = Room.objects.get(slug=request.POST['room'])
        order = Order(
            room=room,
            slug=request.POST['slug'],
            start_date=request.POST['start'],
            finish_date=request.POST['finish'],
            order_cost=request.POST['price'],
            user_name=request.POST['name'],
            phone_number=request.POST['number'],
            email=request.POST['email']
        )
        order.save()

        return redirect('dashboard')


class Edit_order(View):

    def post(self, request):
        room = Room.objects.get(slug=request.POST['room'])
        order = Order.objects.get(id=request.POST['id'])

        order.room = room
        order.slug = request.POST['slug']
        order.start_date = request.POST['start']
        order.finish_date = request.POST['finish']
        order.order_cost = request.POST['price']
        order.user_name = request.POST['name']
        order.phone_number = request.POST['number']
        order.email = request.POST['email']

        order.save()

        return redirect('dashboard')
