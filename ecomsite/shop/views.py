from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Product,Order,OrderItem
from django.http import JsonResponse

# Create your views here.
def index(request):
    products = Product.objects.all()
    search = request.GET.get("search")
    cart = request.session.get("cart", {})
    cart_count = sum(cart.values())
    if search:
        products = products.filter(
            Q(title__icontains=search) |
            Q(category__icontains=search) |
            Q(description__icontains=search)
        )
    paginator = Paginator(products, 4) 
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)
    return render(request,'shop/index.html',{'products':products,
    "cart_count": cart_count,})

def detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,'shop/detail.html',{'product':product})

def add_to_cart(request, id):
    cart = request.session.get("cart", {})
    id = str(id)

    if id in cart:
        cart[id] += 1
    else:
        cart[id] = 1

    request.session["cart"] = cart

    return JsonResponse({
        "count": sum(cart.values())
    })


def cart(request):
    cart = request.session.get("cart", {})
    cart_count = sum(cart.values())

    items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        
        subtotal = product.price * quantity
        total_price += subtotal

        items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    return render(request, "shop/cart.html", {
        "items": items,
        "cart_count": cart_count,
        "total_price": total_price,
    })

def remove_from_cart(request, id):
    cart = request.session.get("cart", {})

    id = str(id)

    if id in cart:
        del cart[id]

    request.session["cart"] = cart

    return redirect("cart")

def increase_quantity(request, id):
    cart = request.session.get("cart", {})

    id = str(id)

    if id in cart:
        cart[id] += 1

    request.session["cart"] = cart

    return redirect("cart")

def decrease_quantity(request, id):
    cart = request.session.get("cart", {})

    id = str(id)

    if id in cart:

        if cart[id] > 1:
            cart[id] -= 1
        else:
            del cart[id]

    request.session["cart"] = cart

    return redirect("cart")

def checkout(request):
    cart = request.session.get("cart", {})

    if not cart:
        return redirect("cart")

    total_price = 0

    order = Order.objects.create(total_price=0)

    for product_id, quantity in cart.items():

        product = Product.objects.get(id=product_id)

        subtotal = product.price * quantity

        total_price += subtotal

        OrderItem.objects.create(order=order,product=product,quantity=quantity,price=product.price,)

    order.total_price = total_price
    order.save()

    request.session["cart"] = {}

    return redirect("index")