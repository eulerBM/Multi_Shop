from django.shortcuts import render
from index.models import product


def index(request):
    procutc_iten = product.objects.all()[:8]
    procutc_recent = product.objects.order_by('-date')[:8]

    context = {

        'product': procutc_iten,
        'product_recen': procutc_recent,
            
    }
    
    return render (request, 'index.html', context)


