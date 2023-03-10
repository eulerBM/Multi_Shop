from django.shortcuts import render
from index.models import product
from django.db.models import Q


def index(request):
    category_iten = product.objects.all()[:8]

    itens_all = product.objects.filter(
    Q(category='Eletrodoméstico') |
    Q(category='Beleza') |
    Q(category='Acessórios') |
    Q(category='Roupas') |
    Q(category='Fantasias') |
    Q(category='Computador')
    )
    print(itens_all)

    product_eletro = product.objects.filter(category='Eletrodoméstico').first()
    


    context = {

        'category':[item[0] for item in product.choices_status[:9]],
        'product': category_iten,
        

            
    }
    
    
    return render (request, 'index.html', context)
