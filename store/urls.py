from django.urls import path
from .views import *

app_name = 'store'

urlpatterns = [
    path('', StoreView.as_view(), name='home'),
    path('product/<slug>/', ProductView.as_view(), name='product'),
    path('add-to-cart/<slug>', add_to_cart, name="add-to-cart"),
    

]