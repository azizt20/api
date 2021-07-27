from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Q
import datetime

from booking.forms import BookingForm
from booking.models import RoomType
from booking.models import Room
from booking.models import Order


class Dashboard(View):
    def get(self, request, start=None):
        datatime_list = []
        asd = datetime.datetime.now() - datetime.timedelta(10)

        start_date = None
        if start is not None:
            start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
            asd = start_date

        for i in range(30):
            datatime_list.append(asd + datetime.timedelta(i))
        # print("------------")
        # for i in datatime_list:
        #     print(i.weekday())
        # print('asdasdasd')
        # print(datetime.date.today().weekday())
        # print('--------------')
        data = {}
        skip = set()

        orders = Order.objects.select_related('room')
        if start is not None:
            orders = orders.filter(Q(start_date__gte=start) | Q(finish_date__gte=start))

        for order in orders.all():
            if start is not None:
                if order.start_date < start_date.date():
                    order.start_date = start_date.date()

            key = "{}_{:%Y-%m-%d}".format(order.room_id, order.start_date)
            data[key] = order

            current = (order.start_date + datetime.timedelta(days=1))
            while current <= order.finish_date:
                key = "{}_{:%Y-%m-%d}".format(order.room_id, current)
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
        return render(request, 'dashboard/dashboard.html', context)

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


def order_list(request):
    content = {
        'orders':Order.objects.order_by('created_at')
    }
    return render(request, 'dashboard/list_orders.html', content)
