from detail.views import detail
from django.urls import path

urlpatterns = [
    path('<int:id>', detail, name='detail' ),
]