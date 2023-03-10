from detail.views import detail
from django.urls import path

urlpatterns = [
    path('', detail, name='detail' ),
]