from django.urls import path

from payments.views import *

urlpatterns = [
    path('home', HomePageView, name='home_paga'),
    path('config/', stripe_config, name='config'),
    path('create-checkout-session/', create_checkout_session, name='create-checkout-session'), 
]