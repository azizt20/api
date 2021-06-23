from django.db import models

# Create your models here.
class TypeRoom(models.Model):
    type = models.CharField

class Room(models.Model):
    typeroom = models.ForeignKey(TypeRoom, on_delete=models.CASCADE())
    room_number = models.IntegerField()
    discription = models.CharField(max_length=200)
    bed_count = models.IntegerField()
    capacity = models.IntegerField()
    cost_per_day = models.IntegerField()

class Date(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE())
    date = models.DateField()

class Order(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE())
    date = models.ForeignKey()
    start_date = models.DateField()
    finish_date = models.DateField()
    count_day = models.IntegerField()
    order_cost = models.IntegerField()
    user_name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

class Items(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE())
    busy = models.BooleanField(default=False)

