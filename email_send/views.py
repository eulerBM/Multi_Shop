from django.shortcuts import render
from django.core.mail import send_mail

def email_newsletter(request):

    if request.method == 'GET':

        send_mail(
        'CADASTRO REALIZADO COM SUCESSO',
        'Voce ira receber noticias sobre descontos, promoção e cupoms parabéns.',
        'eullerborgesdamotta155@gmail.com',
        ['enzelo2002@gmail.com',],
        )

    return render (request, 'index.html')


