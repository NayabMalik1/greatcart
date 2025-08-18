from django.shortcuts import render, redirect
from carts.models import CartItem
from datetime import datetime
from .forms import OrderForm
from .models import Order, OrderProduct
from store.models import Product
from django.core.mail import EmailMessage
from django.template.loader import render_to_string



def place_order(request):
    current_user = request.user
    
    cart_items = CartItem.objects.filter(user=current_user)
    if cart_items.count() <= 0:
        return redirect('store')

    total = 0
    quantity = 0
    tax = 0
    grand_total = 0

    for cart_item in cart_items:  
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    
    tax = (2 * total) / 100
    grand_total = total + tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # ✅ Create Order
            order = Order()
            order.user = current_user
            order.first_name = form.cleaned_data['first_name']
            order.last_name = form.cleaned_data['last_name']
            order.phone = form.cleaned_data['phone']
            order.email = form.cleaned_data['email']
            order.address_line_1 = form.cleaned_data['address_line_1']
            order.address_line_2 = form.cleaned_data['address_line_2']
            order.city = form.cleaned_data['city']
            order.state = form.cleaned_data['state']
            order.country = form.cleaned_data['country']
            order.order_note = form.cleaned_data['order_note']
            order.order_total = grand_total
            order.tax = tax
            order.ip = request.META.get('REMOTE_ADDR')
            order.is_ordered = True   # ✅ Directly mark as ordered (COD)
            order.save()

            # Generate order number
            current_date = datetime.today().strftime("%Y%m%d")
            order_number = current_date + str(order.id)
            order.order_number = order_number
            order.save()

            # ✅ Move cart items to OrderProduct
            for item in cart_items:
                order_product = OrderProduct()
                order_product.order = order
                order_product.user = current_user
                order_product.product = item.product
                order_product.quantity = item.quantity
                order_product.product_price = item.product.price
                order_product.ordered = True
                order_product.save()

                if item.variations.exists():
                    order_product.variations.set(item.variations.all())
                    order_product.save()

                # reduce stock
                product = Product.objects.get(id=item.product.id)
                product.stock -= item.quantity
                product.save()

            # ✅ Clear cart
            CartItem.objects.filter(user=current_user).delete()

            # ✅ Send order confirmation email
            mail_subject = 'Thank you for your order'
            message = render_to_string('orders/order_recieved_email.html', {
                'user': current_user,
                'order': order,
            })
            to_email = current_user.email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            # ✅ Redirect to order complete page
            return redirect('order_complete', order_number=order.order_number)
        else:
            return redirect('checkout')

    else:
        form = OrderForm()
        context = {
            'form': form,
            'cart_items': cart_items,
            'total': total,
            'tax': tax,
            'grand_total': grand_total,
        }
        return render(request, 'orders/payments.html', context)

def order_complete(request, order_number):
    try:
        order = Order.objects.get(order_number=order_number, is_ordered=True)
        ordered_products = OrderProduct.objects.filter(order=order)

        context = {
            'order': order,
            'ordered_products': ordered_products,
        }
        return render(request, 'orders/order_complete.html', context)
    except Order.DoesNotExist:
        return redirect('store')






