from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),

    #Index
    path('', include('index.urls')),

    #Cart
    path('cart', include('cart.urls')),

    #Checkout
    path('checkout', include('checkout.urls')),

    #Detail
    path('detail', include('detail.urls')),

    #Shop
    #Contact
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
