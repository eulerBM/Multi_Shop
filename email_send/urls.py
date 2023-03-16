from django.urls import path
from email_send.views import email_newsletter


urlpatterns = [
    # Email da newsletter - Multishop
    path('newsletter', email_newsletter, name='newsletter'),
 
]