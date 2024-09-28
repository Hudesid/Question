from django.shortcuts import render, HttpResponse
from .forms import QuestionForm
from .models import Question


def question_form_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
        else:
            return HttpResponse('Form is invalid')

    form = {'form': QuestionForm}
    return render(request, 'question_form.html', form)


def success_view(request):
    return render(request, 'question_form.html')


def question_list_view(request):
    questions = Question.objects.all()
    ctx  = {'questions': questions}
    return render(request, 'question_list.html', ctx)
