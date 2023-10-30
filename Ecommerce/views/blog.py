
from django.shortcuts import get_object_or_404,render
from Ecommerce.models import Blog

def blog(request):
    blog_obj = Blog.objects.filter(active=True)
    context = {'page_obj':blog_obj}
    return render(request, 'blog.html', context)


def BlogDetails(request, slug):
    blog_obj = get_object_or_404(Blog,slug=slug)
    context = {'blog_obj':blog_obj }
    return render(request, 'blog-details.html', context)
