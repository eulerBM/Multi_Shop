from django.shortcuts import render
from contact.forms import contact_form

def contact (request):

    return render (request, 'contact.html',{'form':contact_form()})


def save_contato(request):

    if request.method == 'POST': 
        
       
       
        return render(request, 'contact.html')
