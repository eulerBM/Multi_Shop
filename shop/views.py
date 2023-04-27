from django.shortcuts import render
from index.models import product

def shop (request):

    if request.method == 'GET':

        search_query = request.GET.get('search')

        if search_query:
            products = product.objects.filter(name__icontains=search_query)
            
        else:
            products = product.objects.all()

        context = {
            'products': products,
        }

        return render(request, 'shop.html', context)
