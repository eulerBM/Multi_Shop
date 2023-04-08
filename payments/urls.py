from django.urls import path

from payments.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('config/', stripe_config, name='config'),
    path('create-checkout-session/', create_checkout_session),  
]