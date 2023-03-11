from django.shortcuts import render
from index.models import product
from django.db.models import Sum


def index(request):
    category_iten = product.objects.all()

    product_eletro = product.objects.filter(category='Eletrodoméstico').first()
    print(product_eletro)


    context = {

        'category':[item[0] for item in product.choices_status[:9]],
        'product': category_iten,
        

            
    }
    
    
    return render (request, 'index.html', context)
