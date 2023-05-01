from django.shortcuts import render
from index.models import product

def shop (request):

    if request.method == 'GET':

        color = product.objects.all()

        search_query = request.GET.get('search')

        if search_query:
            products = product.objects.filter(name__icontains=search_query)
            
        else:
            products = product.objects.all()

        colors = {
        'black': color.filter(color='Preto'),
        'white': color.filter(color='Branco'),
        'red': color.filter(color='Vermelho'),
        'blue': color.filter(color='Azul'),
        'green': color.filter(color='Verde'),

        }

        size = {
        'pp': color.filter(size='pp'),
        'p': color.filter(size='p'),
        'm': color.filter(size='m'),
        'g': color.filter(size='g'),
        'gg': color.filter(size='gg'),
        'xgg': color.filter(size='xgg'),
        
        }

        price = {
        'p1': color.filter(price__gte=0, price__lte=100),
        'p2': color.filter(price__gte=100, price__lte=500),
        'p3': color.filter(price__gte=500, price__lte=1000),
        'p4': color.filter(price__gte=1000, price__lte=5000),
        'p5': color.filter(price__gt=5000),
        
        }

        context = {
            'products': products,
            'color': colors,
            'size': size,
            'price': price,
        }

        return render(request, 'shop.html', context)
