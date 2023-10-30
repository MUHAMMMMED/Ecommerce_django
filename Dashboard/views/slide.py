from django.shortcuts import render, redirect, get_object_or_404
from Ecommerce.models import Slide
from django.contrib.auth.decorators import login_required
from Dashboard.forms import SlideForm

@login_required
def slide_list(request):
    slide = Slide.objects.all()
    context = {'slide': slide, }
    return render(request, 'slide_list.html', context)



@login_required
def create_or_update_slide(request, slide_id=None):
    if slide_id:
        slide = Slide.objects.get(id=slide_id)
    else:
        slide = Slide()

    if request.method == 'POST':
        form = SlideForm(request.POST, request.FILES, instance=slide)
        if form.is_valid():
            form.save()
            return redirect('slide_list')  # Replace 'slide_list' with the appropriate URL name for your slide list view
    else:
        form = SlideForm(instance=slide)

    return render(request, 'create_or_update_slide.html', {'form': form})

@login_required
def delete_slide(request,slide_id):
    slide = get_object_or_404(Slide, id=slide_id)
    slide.delete()
    return redirect('Dashboard:slide_list')  # Replace 'question_list' with the appropriate URL name for your question list view
