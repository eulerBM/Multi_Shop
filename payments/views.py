from django.shortcuts import render, redirect
from django.conf import settings 
from django.http.response import JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
import stripe


def HomePageView(request):
    return render (request, 'pagamento/home_paga.html')

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':

        stripe_config = {
             
            'publicKey': settings.STRIPE_PUBLISHABLE_KEY
        }

        return JsonResponse(stripe_config, safe=False)
    
@csrf_exempt
def create_checkout_session(request):
        domain_url = 'http://localhost:8000/pagar/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:    
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {   
                        'price':'price_1MsKXsE3RPdMzT3CGMuQAGeX',
                        'quantity': 1,
                        
                    }
                ],
                mode='payment',
                success_url=domain_url + 'sucesso',
                cancel_url=domain_url + 'cancelado',
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
def sucess(request):
    return render (request, 'pagamento/sucess.html')

def cancel(request):
    return render (request, 'pagamento/cancel.html')

