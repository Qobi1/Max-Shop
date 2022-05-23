from django.shortcuts import render, redirect

from shop_app.models import Product
from .forms import ProductForm
from .services import *


def ctg_list(requests, page=None):
    product = get_product(page)
    if product and product['items']:
        ctg = product['items']
    else:
        return False

    meta = product['meta']
    a = meta['count'] // meta['per_page']

    if meta['count'] % meta['per_page']:
        a += 1

    number = [i for i in range(1, a + 1)]

    next = int(meta['current_page']) + 1
    prev = int(meta['current_page']) - 1

    if next > a:
        next = None
    if prev == 0:
        prev = None

    ctx = {
        'product': product,
        'number': number,
        'next': next,
        'prev': prev
    }
    return render(requests, 'dashboard/Product/list.html', ctx)


def ctg_one(requests, pk=None, delete=None):
    product = get_one(pk=pk, delete=delete)
    if delete:
        return redirect('dashboard_product_list')
    ctx = {
        'product': product
    }
    return render(requests, 'dashboard/Product/detail.html', ctx)


def add_edit(requests, pk=None):
    try:
        instance = Product.objects.get(id=pk)
    except:
        instance = None
    form = ProductForm(instance=instance)
    if requests.POST:
        forms = ProductForm(requests.POST, requests.FILES, instance=instance)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard_product_list')
        else:
            print("Error ", forms.errors)
    ctx = {
        'form': form
    }
    return render(requests, 'dashboard/Product/forms.html', ctx)


