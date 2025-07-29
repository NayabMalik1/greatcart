from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Cart, CartItem
from store.models import Product
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.




def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        request.session.create()
        cart_id = request.session.session_key
    return cart_id





def add_cart(request, product_id):
    color = request.GET.get('Color')
    size = request.GET.get('Size')

    if not color or not size:
        return HttpResponse("Color or Size not provided")

    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    # ✅ Check if same variation already exists in cart
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart, color=color, size=size)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
            color=color,
            size=size,
        )
        cart_item.save()

    return redirect('cart')




def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)

    # Get selected color and size (if available)
    color = request.GET.get('Color')
    size = request.GET.get('Size')

    try:
        cart_item = CartItem.objects.filter(
            product=product,
            cart=cart,
            color=color,
            size=size,
        ).first()  # instead of .get()

        if cart_item:
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()

    except:
        pass

    return redirect('cart')



def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = Product.objects.get(id=product_id)
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    return redirect('cart')



def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax=0
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2*total)/100
        grand_total=total+tax
    except ObjectDoesNotExist:
        pass 
        
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total':  grand_total
       
    }
    return render(request, 'store/cart.html', context)