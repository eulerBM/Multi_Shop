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

    #Index - feito
    path('', include('index.urls')),

    #Email - feito
    path("email/", include('email_send.urls')),

    #Cart
    path('cart/', include('cart.urls')),

    #Checkout
    path('checkout/', include('checkout.urls')),

    #Detail - feito
    path('detalhes/', include('detail.urls')),

    #Shop
    path('shop/', include('shop.urls')),

    #Contact - feito
    path('contact/', include('contact.urls')),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
