from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from models import Question, Answer
from forms import AskForm, AnswerForm

# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def questions_all(request):
    questions = Question.objects.order_by('-added_at')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'questions.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })

@require_GET
def popular_questions(request):
    questions = Question.objects.order_by('-rating')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'questions.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })


def question_details(request, question_id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = answer.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
        question = get_object_or_404(Question, id = question_id)
        try:
            answer = question.answer_set.all()
        except Answer.DoesNotExist:
            answer = None
        return render(request, 'question_details.html', {
        'question': question,
        'answer': answer,
        'form': form,
        })


def question_add(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'question_add.html',{
        'form': form,
    })




#initial={'question': question_id}
