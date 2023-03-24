from django.shortcuts import render
from django.core.paginator import Paginator
from index.models import product

def detail(request, id):

    get_product = product.objects.get(id=id)
    paginador = Paginator(get_product, 1)

    context = {

        'products': get_product,
        'paginador': paginador,

    }

    return render (request, 'detail.html', context)
