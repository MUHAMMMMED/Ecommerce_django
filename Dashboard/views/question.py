from django.shortcuts import render, redirect, get_object_or_404
from Ecommerce.models import  Item,Questions
from django.contrib.auth.decorators import login_required
from Dashboard.forms import QuestionsForm

@login_required
def create_question(request,id):

    if not request.user.is_manager():
            return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    item = get_object_or_404(Item, id=id)

    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            question = form.save()  # Save the form and get the saved instance
            item.questions.add(question)  # Add the saved question to the item's questions
            return redirect('Dashboard:update_item', item.id)  # Add a comma here

             # return redirect('question_list')  # Redirect to a view displaying the list of questions
    else:
        form = QuestionsForm()

    return render(request, 'create_question.html', {'form': form})








@login_required
def update_question(request, question_id,item_id):
    if not request.user.is_manager():
            return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    question = get_object_or_404(Questions, pk=question_id)
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = QuestionsForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('Dashboard:update_item', item.id)  # Add a comma here
    else:
        form = QuestionsForm(instance=question)

    return render(request, 'create_question.html', {'form': form})

@login_required
def delete_question(request, question_id,item_id):

    if not request.user.is_manager():
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})

    question = get_object_or_404(Questions, id=question_id)
    item = get_object_or_404(Item, id=item_id)

    question.delete()
    return redirect('Dashboard:update_item', item.id)  # Add a comma here
