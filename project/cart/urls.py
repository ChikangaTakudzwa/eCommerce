from django.urls import path
from cart.views import add_to_cart, cart, checkout, hx_menu_cart


urlpatterns = [
    path('', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('add_to_cart/<int:product_id>', add_to_cart, name="add_to_cart"),
    path('hx_menu_cart/', hx_menu_cart, name="hx_menu_cart")
]