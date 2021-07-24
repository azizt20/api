from django.urls import path, include
from .views import Dashboard, Edit_order

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('post/', Dashboard.as_view(), name='dashboard_post'),
    path('edit/', Edit_order.as_view(), name='edit')
]
