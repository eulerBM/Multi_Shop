from django.urls import path

from payments.views import *

urlpatterns = [
    path('', HomePageView, name='home'),
    path('config/', stripe_config, name='config'),
    path('create-checkout-session/', create_checkout_session),  

    #sucess or cancel
    path('sucesso', sucess, name='sucess'),
    path('cancelado', cancel, name='cancel'),
]