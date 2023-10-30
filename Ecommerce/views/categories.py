from django.shortcuts import get_object_or_404,render,redirect
from Ecommerce.models import Category

def categories(request):
    category = Category.objects.filter(is_active=True)
    context = {'category':category}
    return render(request, 'category.html', context)

def CategoryDetails(request,slug):
    category = get_object_or_404(Category, slug=slug)
    context = {'category':category}
    return render(request, 'categoryid.html', context)
