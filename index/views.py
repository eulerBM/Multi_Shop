from django.shortcuts import render, redirect
from index.models import product, carrinho
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.contrib import messages 

# Pagina Inicial
def index(request):
    procutc_iten = product.objects.all()[:8]
    procutc_recent = product.objects.order_by('-date')[:8]
    car_filter = carrinho.objects.filter(id=request.user.id)

    try:
        car_filter = carrinho.objects.get(car_user=request.user.id)
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

    try:
        product_get = product.objects.get(id=id)

        carrinho_get = carrinho.objects.get(car_user=request.user)
    
    except:
        messages.error(request, "Ocorreu um erro" )

    else:

        if carrinho.objects.filter(car_user=request.user, car_product=product_get):
            messages.warning(request, f"{product_get} ja esta no carrinho!" )

        else:
            carrinho_get.car_product.add(product_get)
            messages.success(request, f"{product_get}, adicionado com sucesso ao carrinho" )     

    finally:
        return redirect ('index')


def like_product(request, id):
    pass


