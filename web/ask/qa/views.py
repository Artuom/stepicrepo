# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from models import Question, Answer, Session
from forms import AskForm, AnswerForm, RegistrationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import random

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
    author_id = Session.objects.get(key = request.COOKIES.get('sessid')).user_id
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        print "form====",form
        if form.is_valid():
            print "in question_details",form
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
            'author':author_id,
            })
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
        'author':author_id,
        })


def question_add(request):
    author_id = Session.objects.get(key = request.COOKIES.get('sessid')).user_id
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
        'author':author_id,
    })


def signup(request):
    print request.POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #form = RegistrationForm(request.POST)
        #print form
        if form.is_valid():
            print "valid"
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        print "not valid"
        form = UserCreationForm()
        #form = RegistrationForm()
    return render(request, "register.html", {
        'form': form,
    })

"""def login_view(request):
    print "request to login", request.POST
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authentificate(username=username, password=password)
        #form = LoginForm(request.POST)

        return HttpResponseRedirect("/")
    else:
        print "not valid"
        form = LoginForm()
    return render(request, "login.html", {
        'form': form,
    })"""

def login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        url = request.POST.get('continue', '/')
        sessid = do_login(username, password)
        print "sessid", sessid
        if sessid:
            response = HttpResponseRedirect(url)
            response.set_cookie('sessid', sessid,
            domain='localhost', httponly=True,
            expires = datetime.now()+timedelta(days=5)
            )
            print "response", response
            return response
        else:
            error = u'Неверный логин / пароль'

    return render(request, 'login.html', {'error': error })


def do_login(username, password):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    """hashed_pass = salt_and_hash(password)
    if user.password != hashed_pass:
        return None"""
    user = authenticate(username=username, password=password)
    print "USER IS",user
    if not user:
        return None
    session = Session()
    session.key = "sdfsdfsdfkgkvnblkdfhlsghfhfvbnkn" + str(random.randint(1,100))
    session.user = user
    session.expires = datetime.now() + timedelta(days=5)
    session.save()
    return session.key
#initial={'question': question_id}
