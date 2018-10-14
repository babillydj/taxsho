from django.urls import reverse
from django.shortcuts import render

from apps.product.models import Product


def landing(request):
    context = {}
    context['products'] = Product.objects.all()
    return render(request, 'index.html', context)

def doc(request):
    context = {}
    return render(request, 'doc.html', context)
