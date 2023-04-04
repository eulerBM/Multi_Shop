from index.views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index' ),

    #like no produto
    path('like/', like_product, name='like'),

    #Atualizar produto
    path('atualizar/<int:id>', update_product, name='update_product'),

    #Adicionar no carrinho
    path('carrin/', add_to_cart, name='carrin'),

    
]
