from django.shortcuts import render, redirect, get_object_or_404
from Ecommerce.models import Blog
from django.contrib.auth.decorators import login_required
from Dashboard.forms import BlogForm

@login_required
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})


@login_required
def create_or_update_blog(request, blog_id=None):
    if blog_id:
        blog = Blog.objects.get(id=blog_id)
    else:
        blog = Blog()

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            title = blog.Titel.replace(" ", "_")  # Remove spaces from the title
            blog.slug = title
            blog.save()
            return redirect('Dashboard:blog_list')  # Replace 'blog_list' with the appropriate URL name for your blog list view
    else:
        form = BlogForm(instance=blog)

    return render(request, 'create_or_update_blog.html', {'form': form})
@login_required
def delete_blog(request,blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('Dashboard:blog_list')  # Replace 'question_list' with the appropriate URL name for your question list view
