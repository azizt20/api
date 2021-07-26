from django.urls import path, include, re_path
from .views import Dashboard, Edit_order, order_list

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    re_path('(?P<start>\d{4}-\d{2}-\d{2})/', Dashboard.as_view(), name='dashboard'),
    path('post/', Dashboard.as_view(), name='dashboard_post'),
    path('edit/', Edit_order.as_view(), name='edit'),
    path('order-list/', order_list, name="order_list")

]
