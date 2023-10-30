from django.shortcuts import render, redirect, get_object_or_404
from Ecommerce.models import Info
from django.contrib.auth.decorators import login_required
from Dashboard.forms import InfoForm

@login_required
def info_list(request):
    info_list = Info.objects.all()
    context = {'info_list': info_list}
    return render(request, 'info_list.html', context)
@login_required
def create_or_update_info(request, info_id=None):
    info = None
    if info_id:
        info = get_object_or_404(Info, pk=info_id)

    if request.method == 'POST':
        form = InfoForm(request.POST, request.FILES, instance=info)
        if form.is_valid():
            form.save()
            return redirect('Dashboard:info_list')  # Redirect to the list view after successful creation/update
    else:
        form = InfoForm(instance=info)

    context = {'form': form, 'info': info}
    return render(request, 'create_or_update_info.html', context)

@login_required
def delete_info(request,info_id):
    info_list = get_object_or_404(Info, id=info_id)
    info_list.delete()
    return redirect('Dashboard:info_list')
