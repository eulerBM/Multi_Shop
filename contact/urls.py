from django.urls import path
from contact.views import *


urlpatterns = [
    path('', contact),
    path('enviar', save_contato, name='enviar' ),
   
    

]