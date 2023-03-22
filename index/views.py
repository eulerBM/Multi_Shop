from django.shortcuts import render, redirect
from index.models import product, carrinho, User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET

# Pagina Inicial
def index(request):
    procutc_iten = product.objects.all()[:8]
    procutc_recent = product.objects.order_by('-date')[:8]
    car_filter = carrinho.objects.filter(id=request.user.id)

    try:
        car_filter = carrinho.objects.get(id=request.user.id)
        carrinho_filter = car_filter.car_product.all().count()

    except:
        carrinho_filter = int(0)
         
    context = {

        'product': procutc_iten,
        'product_recen': procutc_recent,
        'car_filter': carrinho_filter,
            
    }
 
    return render (request, 'index.html', context)



@require_GET
@login_required
def add_car (request, id):
    product_get = product.objects.get(id=id)

    carrinho_get = carrinho.objects.get(car_user=request.user)

    carrinho_get.car_product.add(product_get)
    
    return redirect ('index')
    


