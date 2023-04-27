from django.shortcuts import render
from index.models import product

def shop (request):

    if request.method == 'GET':

        context = {
        'products': product.objects.all(),  

        }

        return render (request, 'shop.html', context)
