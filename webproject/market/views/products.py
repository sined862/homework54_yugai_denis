from django.shortcuts import render
from market.models import Product, Category
from django.shortcuts import redirect , get_object_or_404


def detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product})


def add_product_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request,'product_create.html',context={
            'categories': categories
        })
    product_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'price': request.POST.get('price'),
        'image': request.POST.get('image'),
        'category_id': request.POST.get('category_id'),
    }
    product = Product.objects.create(**product_data)
    return redirect('product_detail', pk=product.pk)