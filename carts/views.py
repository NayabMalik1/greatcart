from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Cart, CartItem
from store.models import Product
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.




def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        request.session.create()
        cart_id = request.session.session_key
    return cart_id





from django.http import HttpResponse
from django.shortcuts import redirect
from store.models import Product
from .models import Cart, CartItem
from .views import _cart_id


def add_cart(request, product_id):
    current_user = request.user

    # Get variation data from URL
    color = request.GET.get('Color')
    size = request.GET.get('Size')

    if not color or not size:
        return HttpResponse("Color or Size not provided")

    # Get product
    product = Product.objects.get(id=product_id)

    # ---------------- AUTHENTICATED USER ----------------
    if current_user.is_authenticated:
        cart_items = CartItem.objects.filter(
            product=product,
            user=current_user,
            color=color,
            size=size
        )

        if cart_items.exists():
            cart_item = cart_items.first()
            cart_item.quantity += 1
            cart_item.save()
        else:
            CartItem.objects.create(
                product=product,
                user=current_user,
                quantity=1,
                color=color,
                size=size
            )
        return redirect('cart')

    # ---------------- NON-AUTHENTICATED USER ----------------
    else:
        # Get or create a cart for session
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=_cart_id(request))
            cart.save()

        cart_items = CartItem.objects.filter(
            product=product,
            cart=cart,
            color=color,
            size=size
        )

        if cart_items.exists():
            cart_item = cart_items.first()
            cart_item.quantity += 1
            cart_item.save()
        else:
            CartItem.objects.create(
                product=product,
                cart=cart,
                quantity=1,
                color=color,
                size=size
            )

        return redirect('cart')



def remove_cart(request, product_id):
    current_user = request.user
    product = get_object_or_404(Product, id=product_id)

    color = request.GET.get('Color')
    size = request.GET.get('Size')

    if current_user.is_authenticated:
        # Logged-in user
        cart_item = CartItem.objects.filter(
            product=product,
            user=current_user,
            color=color,
            size=size
        ).first()
    else:
        # Guest user
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            return redirect('cart')  # No cart, nothing to remove

        cart_item = CartItem.objects.filter(
            product=product,
            cart=cart,
            color=color,
            size=size
        ).first()

    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart')


def remove_cart_item(request, product_id):
    current_user = request.user
    product = get_object_or_404(Product, id=product_id)

    color = request.GET.get('Color')
    size = request.GET.get('Size')

    if current_user.is_authenticated:
        # Logged-in user
        cart_item = CartItem.objects.filter(
            product=product,
            user=current_user,
            color=color,
            size=size
        ).first()
    else:
        # Guest user
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            return redirect('cart')  # No cart, nothing to remove

        cart_item = CartItem.objects.filter(
            product=product,
            cart=cart,
            color=color,
            size=size
        ).first()

    if cart_item:
        cart_item.delete()

    return redirect('cart')




def cart(request, total=0, quantity=0, cart_items=None):
    tax = 0
    grand_total = 0  # ✅ default value set
    cart_items = []
    try:
        if request.user.is_authenticated:
              cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total) / 100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total
    }
    return render(request, 'store/cart.html', context)

from carts.models import CartItem
from carts.views import _cart_id

@login_required(login_url='login')
def checkout(request):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    except Cart.DoesNotExist:
        cart_items = []

    total = 0
    quantity = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

    context = {
        'cart_items': cart_items,
        'total': total,
        'quantity': quantity,
    }
    return render(request, 'store/checkout.html', context)
