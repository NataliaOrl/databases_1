from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort_value = request.GET.get('sort')
    if sort_value == 'min_price':
        phones = phones.order_by('price')
    elif sort_value == 'max_price':
        phones = phones.order_by('-price')
    elif sort_value == 'name':
        phones = phones.order_by('name')
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    my_phone = Phone.objects.get(slug=slug)
    context = {'phone': my_phone}
    return render(request, template, context)
