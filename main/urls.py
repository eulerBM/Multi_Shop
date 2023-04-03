from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),

    #Pagamento
    path('pagar/', include('payments.urls')), 

    #Avatar
    path('avatar/', include('avatar.urls')),

    #Allauth
    path('accounts/', include('allauth.urls')),

    #Index
    path('', include('index.urls')),

    #Email
    path("email/", include('email_send.urls')),

    #Cart
    path('cart/', include('cart.urls')),

    #Checkout
    path('checkout/', include('checkout.urls')),

    #Detail
    path('detalhes/', include('detail.urls'), ),

    #Shop
    #Contact
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
