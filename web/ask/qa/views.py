from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from models import Question, Answer

# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def questions_all(request):
    questions = Question.objects.order_by('added_at')
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
    print question
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'questions.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })

@require_GET
def question_details(request, question_id):
    #question_id = kwargs[question_id]
    #print question_id
    question = get_object_or_404(Question, id = question_id)
    try:
        #answer = Answer.question_set.all()
        answer = question.answer_set.all()
    except Answer.DoesNotExist:
        answer = None
    return render(request, 'question_details.html', {
    'question': question,
    'answer': answer,
    })
