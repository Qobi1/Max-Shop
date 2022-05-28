from django.shortcuts import render, redirect

from shop_app.models import Category
from .forms import CtgForm
from .services import *


def ctg_list(requests, page=None):
    print('page>>>>>>>>', page)
    ctgs = get_ctg(page)
    print('>>>>>>>>>>>>>>>>>>>', ctgs)
    if ctgs and ctgs['items']:
        ctg = ctgs['items']
    else:
        return False

    meta = ctgs['meta']
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
    print('>>>', ctg)
    ctx = {
        'ctgs': ctg,
        'number': number,
        'next': next,
        'prev': prev
    }
    return render(requests, 'dashboard/Category/list.html', ctx)


def ctg_one(requests, pk=None, delete=None):
    ctg = get_one(pk=pk, delete=delete)
    print(ctg)
    if delete:
        return redirect('dashboard_ctg_list')
    ctx = {
        'ctg': ctg
    }
    return render(requests, 'dashboard/Category/details.html', ctx)


def add_edit(requests, pk=None):
    try:
        instance = Category.objects.get(id=pk)
    except:
        instance = None
    form = CtgForm(instance=instance)
    if requests.POST:
        forms = CtgForm(requests.POST, requests.FILES, instance=instance)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard_ctg_list')
        else:
            print("Error ", forms.errors)
    ctx = {
        'form': form
    }
    return render(requests, 'dashboard/Category/forms.html', ctx)


