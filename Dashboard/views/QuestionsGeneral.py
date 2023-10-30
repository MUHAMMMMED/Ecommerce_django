from django.shortcuts import render, redirect, get_object_or_404
from Ecommerce.models import QuestionsGeneral
from django.contrib.auth.decorators import login_required
from Dashboard.forms import QuestionsGeneralForm


@login_required
def question_list(request):
    questions = QuestionsGeneral.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'question_list.html', context)

@login_required
def create_or_update_question(request, question_id=None):
    if question_id:
        question = QuestionsGeneral.objects.get(id=question_id)
        form = QuestionsGeneralForm(request.POST or None, instance=question)
    else:
        form = QuestionsGeneralForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Dashboard:question_list')  # Replace 'question_list' with the appropriate URL name for your question list view

    context = {
        'form': form,
    }
    return render(request, 'create_question.html', context)



@login_required
def delete_question(request, question_id):
    question = get_object_or_404(QuestionsGeneral, id=question_id)
    question.delete()
    return redirect('Dashboard:question_list')  # Replace 'question_list' with the appropriate URL name for your question list view
