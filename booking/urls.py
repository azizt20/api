from django.urls import path, include
from booking import views

urlpatterns = [
    path('order/', views.OrderList.as_view()),
    path('room/', views.RoomList.as_view()),
    path('roomtype/', views.RoomTypeList.as_view()),
    path('order1/', views.Order1List.as_view()),
    path('room1/', views.Room1List.as_view()),
    path('roomtype1/', views.RoomType1List.as_view()),
    path('date/', views.RoomType1List.as_view()),
]