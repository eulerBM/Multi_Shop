from django.shortcuts import render
from contact.forms import contact_form

def contact (request):

    if request.method == 'GET':

        return render (request, 'contact.html',{'form': contact_form()})
    
    else:
        form = contact_form(request.POST)

        if form.is_valid():
            form.save()
            form_new = contact_form
            
            return render(request, 'contact.html', {'form': form_new})
        
       
        return render(request, 'contact.html')


