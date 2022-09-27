from django.shortcuts import render
from market.models import Category
from django.shortcuts import redirect , get_object_or_404


def add_category_view(request):
    if request.method == 'GET':
        return render(request,'category_create.html')
    category_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description')
    }
    task = Category.objects.create(**category_data)
    return redirect('index')