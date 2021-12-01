from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
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
    context = {
        'cart': request.session.get('cart', False)
    }
    return HttpResponse(template.render(context, request))

# add to cart endpoint
def add_to_cart(request, item_id):
    # add the item to the cart
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + 1
    request.session['cart'] = cart
    return HttpResponseRedirect('/cart')

