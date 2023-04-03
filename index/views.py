from django.shortcuts import render, redirect
from index.models import product, carrinho
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.contrib import messages 

# Pagina Inicial
def index(request):
    procutc_iten = product.objects.filter(active=True)[:8]
    procutc_recent = product.objects.order_by('-date').filter(active=True)[:8]
    like_filter = product.objects.filter(likes=request.user.id).count()

    try:
        car_filter = carrinho.objects.get(car_user=request.user.id)
        carrinho_filter = car_filter.car_product.all().count()

    except:
        carrinho_filter = int(0)
    
    
         
    context = {

        'product': procutc_iten,
        'product_recen': procutc_recent,
        'car_filter': carrinho_filter,
        'like': like_filter,
            
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


@require_GET
@login_required
def like_product(request, id):

    try:
        product_get = product.objects.get(id=id)

    except:
        messages.error(request, "Ocorreu um erro" )

    else:
        if product_get.likes == request.user:
            product_get.likes = None
            product_get.save()    
            messages.info(request, f" Voce desfez o like no {product_get}" )

        else:
            product_get.likes = request.user
            product_get.save()
            messages.success(request, f"Like no produto {product_get}" )     

    finally:
        return redirect ('index')
    
@require_GET
@login_required
def update_product(request, id):

    try:
        get_produ = product.objects.get(id=id)
        get_produ.active = False
        get_produ.save()

    except:
        messages.error(request, "Não deu pra atualizar a lista" )

    finally:
        return redirect ('index')

    

from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


#Teste js

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data['id']
        user = data['request']

        if not carrinho.objects.filter(car_user=user, car_product=product_id):
        
            product_get = product.objects.get(id=product_id)
            carrinho_get = carrinho.objects.get(car_user=user)

            carrinho_get.car_product.add(product_get)
        
        
            return JsonResponse({'message': 'Produto adicionado ao carrinho com sucesso!'})

    
    return JsonResponse({'error': 'Esse produto ja foi adicionado no carrinho'}, status=400)


        



