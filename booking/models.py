import datetime

from django.db import models


# Create your models here.
class TypeRoom(models.Model):
    type = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.type}'


class Room(models.Model):
    typeroom = models.ForeignKey(TypeRoom, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    description = models.CharField(max_length=200)
    bed_count = models.IntegerField()
    capacity = models.IntegerField()
    cost_per_day = models.IntegerField()

    def __str__(self):
        return f'{self.typeroom} {self.room_number} '


class Order(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    order_number = models.IntegerField(blank=True, null=True)
    start_date = models.DateField()
    finish_date = models.DateField()
    count_day = models.IntegerField()
    order_cost = models.IntegerField()
    user_name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.room_number}'


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    busy = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.busy}'
