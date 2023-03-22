from index.views import index, add_car
from django.urls import path

urlpatterns = [
    path('', index, name='index' ),
    
    path('<int:id>', add_car, name='add_car'),
    
]
