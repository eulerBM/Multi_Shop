from django.shortcuts import render
from contact.forms import contact_form
from index.models import carrinho, product

def contact (request):

    if request.method == 'GET':

        if request.user.is_authenticated:
            like = product.objects.filter(likes=request.user).count()
            carrin = carrinho.objects.get(car_user=request.user.id).car_product.count()

        else:
            like = 0
            carrin = 0

        context = {
        'form': contact_form(),
        'like': like,
        'carrin': carrin,
        }

        return render (request, 'contact.html', context)
    
    else:
        form = contact_form(request.POST)

        if form.is_valid():
            form.save()
            form_new = contact_form
            
            return render(request, 'contact.html', {'form': form_new})
        
       
        return render(request, 'contact.html')


