from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic

from shop.models import Product


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def index(request):
    latest_product_list = Product.objects.order_by('-created_at')
    template = loader.get_template('index.html')
    context = {
        'products': latest_product_list,
    }
    return HttpResponse(template.render(context, request))

# shopping cart page
def cart(request):
    template = loader.get_template('cart.html')
    cart = request.session.get('cart', {})
    items = []
    for key in cart:
        # if the quantity is less than 1, skip
        if cart[key] < 1:
            continue

        # get the product object
        product = Product.objects.get(pk=key)
        item = {
            'quantity': cart[key],
            'product': product,
        }
        items.append(item)
    context = {
        'cart': items
    }
    return HttpResponse(template.render(context, request))

# add to cart endpoint
def add_to_cart(request, item_id):
    # add the item to the cart
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + 1
    request.session['cart'] = cart
    return HttpResponseRedirect('/cart')

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) - 1
    if cart[item_id] == 0:
        del cart[item_id]
    request.session['cart'] = cart
    print(request.session['cart'])
    return HttpResponseRedirect('/cart')
