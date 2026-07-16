from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    search = request.GET.get("search")

    if search:
        products = products.filter(
            Q(title__icontains=search) |
            Q(category__icontains=search) |
            Q(description__icontains=search)
        )
    paginator = Paginator(products, 4) 
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)
    return render(request,'shop/index.html',{'products':products})

def detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,'shop/detail.html',{'product':product})