from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from shop.models import Product

def index(request):
    latest_product_list = Product.objects.order_by('-created_at')
    template = loader.get_template('index.html')
    context = {
        'latest_product_list': latest_product_list,
    }
    return HttpResponse(template.render(context, request))

# shopping cart page
def cart(request):
    template = loader.get_template('cart.html')
    context = {}
    return HttpResponse(template.render(context, request))