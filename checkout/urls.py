from checkout.views import checkout
from django.urls import path

urlpatterns = [
    path('', checkout, name='checkout' ),
]