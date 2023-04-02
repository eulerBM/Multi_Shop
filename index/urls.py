from index.views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index' ),

    #carrinho
    path('carrinho/<int:id>', add_car, name='add_car'),

    #like no produto
    path('like/<int:id>', like_product, name='like_product'),

    #Atualizar produto
    path('atualizar/<int:id>', update_product, name='update_product')
    
]
