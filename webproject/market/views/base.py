from django.shortcuts import render
from market.models import Category, Product

def index_view(request):
    products = Product.objects.all().order_by('created_at').reverse
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'index.html', context)