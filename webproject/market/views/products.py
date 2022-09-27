from django.shortcuts import render
from market.models import Product
from django.shortcuts import redirect , get_object_or_404


def detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product})