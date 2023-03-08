from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #Index
    path('', include('index.urls'))

    #Shop
    #Detail
    #Contact
    #Checkout
    #Cart

]
