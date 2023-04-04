from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from index.models import product, review_person, carrinho
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required


def detail(request, id):

    try:
        # item product
        get_product = product.objects.get(id=id)

        # Review
        get_review = review_person.objects.filter(product_review=id)

        #likes e carrinho
        likes_count = product.objects.filter(likes=request.user).count()
        carrinho_count = carrinho.objects.get(car_user=request.user)

    except:
        return redirect ('index')

    else:
        user_paginator = Paginator(get_review, 1)
        page = request.GET.get('page')
        posts = user_paginator.get_page(page)
        

        context = {

            'products': get_product,
            'posts': posts,
            'likes': likes_count,
            'carrinho': carrinho_count.car_product.count(),

        }

        return render (request, 'detail.html', context)



@login_required
@require_GET
def review(request, id):

    try:
        get_text = request.GET.get('text')
        get_product = product.objects.get(id=id)

    except:
        return redirect ('index')
    
    else: 
        review_person.objects.create(
            person = request.user,
            product_review = get_product,
            text = get_text,
        )

        return redirect ('detail', id)
