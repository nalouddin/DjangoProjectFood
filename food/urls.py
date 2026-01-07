from django.urls import path
from .views import home, item_detail

urlpatterns = [
    path('', home, name='home'),
    path('item/<int:pk>/', item_detail, name='item_detail'),
]