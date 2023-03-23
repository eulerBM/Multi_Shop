from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from index.models import product, carrinho
from django.contrib.auth.models import User
from index.funções_personalizadas import criar_carrinho

@receiver(pre_save, sender=product)
def price_format(sender, instance, **kwargs):
        
        if instance.price:   
            instance.price = round(instance.price)         

        else:
            pass


@receiver(post_save, sender=User)
def create_carrinho(sender, created, instance, **kwargs):
    
    if created:
         criar_carrinho(user=instance)
    else:
        if not carrinho.objects.filter(car_user = instance):
            criar_carrinho(user=instance)
        
             
         
    

    
         
     
     
     
     
     
