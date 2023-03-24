from index.views import index, add_car, like_product
from django.urls import path

urlpatterns = [
    path('', index, name='index' ),

    #carrinho
    path('carrinho/<int:id>', add_car, name='add_car'),

    #like no produto
    path('like/<int:id>', like_product, name='like_product')
    
]
