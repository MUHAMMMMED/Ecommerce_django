from django.shortcuts import render, redirect, get_object_or_404
from Ecommerce.models import  Item
from django.contrib.auth.decorators import login_required
from Dashboard.forms import ItemForm





@login_required
def items(request):
    if not request.user.is_manager():
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    Items =Item.objects.all()
    context = {'Items': Items, }
    return render(request, 'ItemDASH.html', context)



@login_required
def create_item(request):

    if not request.user.is_manager():
            return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            title = item.title.replace(" ", "_")  # Remove spaces from the title
            item.slug = title
            item.save()
            return redirect('Dashboard:items')  # Redirect to a success page or another view
    else:
        form = ItemForm()

    return render(request, 'create_item.html', {'form': form})


@login_required
def update_item(request, item_id):
    if not request.user.is_manager():
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            title = item.title.replace(" ", "_")  # Remove spaces from the title
            item.slug = title
            item.save()
            return redirect('Dashboard:items')  # Redirect to a success page or another view

    else:
        form = ItemForm(instance=item)

    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'update_item.html', context)







@login_required
def delete_item(request, item_id):

    if not request.user.is_manager():
         return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('Dashboard:items')  # Redirect to a success page or another view
    context={'item':item}

    return render(request, 'Delete.html',context)
