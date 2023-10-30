from django.shortcuts import get_object_or_404,render
from Ecommerce.models import Item,Category,Blog
import random


def home(request):
    category = Category.objects.filter(is_active=True)
    items = Item.objects.filter(is_active=True).order_by('-created_at')
    blog_obj = Blog.objects.filter(active=True).order_by('?')[:4]
    context = {'category':category,'items':items,'page_obj':blog_obj }
    return render(request, 'index.html', context)
