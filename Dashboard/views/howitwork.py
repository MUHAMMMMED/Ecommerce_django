from django.shortcuts import render, redirect, get_object_or_404
from Ecommerce.models import  Item,Howitwork
from django.contrib.auth.decorators import login_required
from Dashboard.forms import HowitworkForm

@login_required
def create_howitwork(request, item_id):
    if not request.user.is_manager():
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = HowitworkForm(request.POST, request.FILES)
        if form.is_valid():
            how = form.save()
            item.howitwork.add(how)  # Add the saved howitwork instance to the item's how field

            return redirect('Dashboard:update_item', item_id)
    else:
        form = HowitworkForm()

    return render(request, 'create_howitwork.html', {'form': form})


@login_required
def update_howitwork(request,howitwork_id, item_id):

    if not request.user.is_manager():
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    howitwork = get_object_or_404(Howitwork,pk=howitwork_id)
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = HowitworkForm(request.POST, request.FILES, instance=howitwork)
        if form.is_valid():
            form.save()

            return redirect('Dashboard:update_item', item.id)  # Add a comma here
    else:
        form = HowitworkForm(instance=howitwork)

    return render(request, 'create_howitwork.html', {'form': form})



@login_required
def delete_howitwork(request,howitwork_id,item_id):

    if not request.user.is_manager():
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    How = get_object_or_404(Howitwork, id=howitwork_id)
    item = get_object_or_404(Item, id=item_id)
    How.delete()

    return redirect('Dashboard:update_item', item.id)  # Add a comma here
