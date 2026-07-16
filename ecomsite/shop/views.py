from django.shortcuts import render
from django.db.models import Q
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
    return render(request,'shop/index.html',{'products':products})