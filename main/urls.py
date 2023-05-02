from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Admin - feito
    path('admin/', admin.site.urls),

    #Pagamento - feito
    path('pagar/', include('payments.urls')), 

    #Avatar - feito
    path('avatar/', include('avatar.urls')),

    #Allauth - feito
    path('accounts/', include('allauth.urls')),

    #Index - feito
    path('', include('index.urls')),

    #Email - feito
    path("email/", include('email_send.urls')),

    #Detail - feito
    path('detalhes/', include('detail.urls')),

    #Shop
    path('shop/', include('shop.urls')),

    #Contact - feito
    path('contact/', include('contact.urls')),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
