from index.models import carrinho

#Função pra criar Usuario - Signals
def criar_carrinho(user):
     carrinho.objects.create (
              car_user = user,
            )
