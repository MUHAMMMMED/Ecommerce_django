from django.shortcuts import render, redirect, get_object_or_404
from Ecommerce.models import  Category
from django.contrib.auth.decorators import login_required
from Dashboard.forms import CategoryForm

@login_required
def categories(request):

    if not request.user.is_manager():
            return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    category = Category.objects.all()
    context = {'category':category}
    return render(request, 'CategoryDASH.html', context)
#
@login_required
def create_category(request):
    if not request.user.is_manager():
         return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            title = category.title.replace(" ", "_")  # Remove spaces from the title
            category.slug = title
            category.save()
            # Redirect or do something else after successful creation
            return redirect('Dashboard:category')
    else:
        form = CategoryForm()

    context = {
        'form': form
    }
    return render(request, 'create_category.html', context)

@login_required
def update_category(request,id):

    if not request.user.is_manager():
            return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    category = get_object_or_404(Category, id=id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            title = category.title.replace(" ", "_")  # Remove spaces from the title
            category.slug = title
            category.save()
            # Redirect or do something else after successful update
            return redirect('Dashboard:category')

    else:
        form = CategoryForm(instance=category)

    context = {
        'form': form,
        'category': category
    }
    return render(request, 'create_category.html', context)


@login_required
def delete_category(request,id):

    if not request.user.is_manager():
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('Dashboard:category')  # Redirect to a success page or another view
    context={'category':category}
    return render(request, 'Deletecat.html',context)
