from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:item_id>', views.add_to_cart, name='add_to_cart'),
    path('accounts/', include('django.contrib.auth.urls'))
]