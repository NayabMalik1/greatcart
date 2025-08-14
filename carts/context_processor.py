from carts.views import _cart_id
from .models import Cart, CartItem

def counter(request):
    cart_count = 0
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            cart_count += item.quantity
    except:
        cart_count = 0
    return dict(cart_count=cart_count)

