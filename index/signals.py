from django.dispatch import receiver
from django.db.models.signals import pre_save
from index.models import product
import math



@receiver(pre_save, sender=product)
def price_format(sender, instance, **kwargs):
        if instance.price:   
            instance.price = round(instance.price)         

        else:
            pass

   
 