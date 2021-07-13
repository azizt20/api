import datetime

from django.db import models


# Create your models here.
class RoomType(models.Model):
    type = models.CharField(max_length=50, blank=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return f'/{self.slug}'

    def __str__(self):
        return f'{self.type}'


class Room(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    slug = models.SlugField()
    description = models.CharField(max_length=200)
    bed_count = models.IntegerField()
    capacity = models.IntegerField()
    cost_per_day = models.IntegerField()

    def get_absolute_url(self):
        return f'/{self.room_type.slug}/{self.slug}'

    def __str__(self):
        return f'{self.room_type} {self.room_number} '


class Order(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    slug = models.SlugField()
    start_date = models.DateField()
    finish_date = models.DateField()
    count_day = models.IntegerField()
    order_cost = models.IntegerField()
    user_name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def get_absolute_url(self):
        return f'/{self.room.room_type.slug}/{self.room.slug}/{self.slug}'




class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    busy = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.busy}'
