from django.conf.urls import patterns, url

from qa import views

urlpatterns = patterns('',

    #url(r'^', views.test, name='test'),
    url(r'^index.html', views.questions_all, name='questions_all'),
    url(r'^login', views.login_view, name='login_view'),
    url(r'^ask', views.question_add, name='question_add'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^popular', views.popular_questions, name='popular_questions'),
    url(r'^new', views.test, name='test'),
    url(r'^answer/(?P<question_id>\d+)', views.question_details, name='question_details'),
    url(r'^question/(?P<question_id>\d+)', views.question_details, name='question_details'),
    #url(r'^question/(?P<question_id>\d+)$', views.test, name='test'),
    #url(r'^', views.questions_all, name='questions_all'),

)

"""
/
/login/
/signup/
/question/<123>/
/ask/
/popular/
/new/
"""
