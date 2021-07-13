from django.contrib import admin
from .models import Room, RoomType, Order, Item

admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Order)
admin.site.register(Item)
