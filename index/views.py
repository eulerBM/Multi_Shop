from django.shortcuts import render, redirect
from index.models import product, carrinho, User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET,require_POST
from django.contrib import messages 
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


# Pagina Inicial
def index(request):
    procutc_iten = product.objects.filter(active=True)[:8]
    procutc_recent = product.objects.order_by('-date').filter(active=True)[:8]

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

    key = request.session.get('email')
    print(request.session.session_key) 
 
    return render (request, 'index.html', context)


# Like no produto
@login_required
@require_POST
@csrf_exempt
def like_product(request):
    if request.method == 'POST':

        try:
            data = json.loads(request.body)
            id_ = data['id']
            user = data['request']

        except:
            return JsonResponse({'message': 'Ocorreu um erro'})
        
        else:
            if product.objects.filter(id=id_, likes=user):
                return JsonResponse({'message': 'Voce ja deu like nesse produto'})
            
            else:
                produ = product.objects.get(id=id_)
                user_get = User.objects.get(id=user)
                produ.likes = user_get
                produ.save()
                print('voce deu like')

                return JsonResponse({'message': 'Like dado com sucesso'})
    
    return JsonResponse({'error': 'O metodo nao foi POST'}, status=400)


# Atualiza o produto da pagina
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


# Adiociona o produto no carrinho

@require_POST
@csrf_exempt
@login_required
def add_to_cart(request):
    if request.method == 'POST':

        try:
            data = json.loads(request.body)
            product_id = data['id']
            user = data['request']

        except:
            return JsonResponse({'message': 'Ocorreu um erro'})
        
        else:
            if carrinho.objects.filter(car_user=user, car_product=product_id):
      
                return JsonResponse({'message': 'Esse produto ja esta no carrinho'})
            
            else:
                product_get = product.objects.get(id=product_id)
                carrinho_get = carrinho.objects.get(car_user=user)
                carrinho_get.car_product.add(product_get)
            
                return JsonResponse({'message': 'Produto adicionado ao carrinho com sucesso!'})
    
    return JsonResponse({'error': 'Só aceitamos metodos POST'}, status=400)


        



