import zipbay.settings as settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:item_id>', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>', views.remove_from_cart, name='remove_from_cart'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('isp/prj/prj.html', views.redirect_to_index, name='redirect_to_index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
