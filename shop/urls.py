from django.urls import path
from shop.views import shop

urlpatterns = [

    path('', shop, name='shop'),

]