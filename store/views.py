from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from orders.models import OrderProduct


from carts.models import Cart, CartItem
from carts.views import _cart_id
from .models import Product
from category.models import category 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import ReviewRating
from django.contrib import messages
from .forms import ReviewForm 
 # lowercase model name as you used


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(category, slug=category_slug)  
        products = Product.objects.filter(category=categories, is_available=True)
        paginator=Paginator(products, 1)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.filter(is_available=True)
        paginator=Paginator(products, 3)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
        product_count = products.count()

    context = {
        'products':  paged_products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        cart = Cart.objects.get(cart_id=_cart_id(request))
        in_cart_items = CartItem.objects.filter(product=single_product, cart=cart)
    except Cart.DoesNotExist:
        in_cart_items = []

    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(
                user=request.user, product_id=single_product.id
            ).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = False
    else:
        orderproduct = False

    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)
    average_rating = single_product.averageReview()

    context = {
        'single_product': single_product,
        'in_cart_items': in_cart_items,
        'orderproduct': orderproduct,
        'reviews': reviews,
        'average_rating': average_rating,
    }
    return render(request, 'store/product_detail.html', context)





from django.db.models import Q
from .models import Product

def search(request):
    keyword = request.GET.get('keyword')
    products = []
    product_count = 0

    if keyword:
        products = Product.objects.filter(
            Q(product_name__icontains=keyword) | Q(description__icontains=keyword),
            is_available=True
        )
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)

def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')  # Get the URL of the previous page
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            if form.is_valid():
                form.save()
                messages.success(request, 'Thank you! Your review has been updated.')
                return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.product_id = product_id
                data.user_id = request.user.id
                data.subject = form.cleaned_data['subject']
                data.review = form.cleaned_data['review']
                data.rating = form.cleaned_data['rating']
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)


from django.shortcuts import render
from orders.models import Order, OrderProduct

def my_orders(request):
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    
    # har order ke sath uske items attach kar rahe hain
    orders_with_items = []
    for order in orders:
        items = OrderProduct.objects.filter(order=order)
        orders_with_items.append({
            'order': order,
            'items': items,
        })

    context = {
        'orders_with_items': orders_with_items,
    }
    return render(request, 'dashboard.html', context)




        
      
