from django.conf.urls import patterns, url

from qa import views

urlpatterns = patterns('',

    #url(r'^', views.test, name='test'),

    url(r'^login', views.test, name='test'),
    url(r'^ask', views.test, name='test'),
    url(r'^signup', views.test, name='test'),
    url(r'^popular', views.popular_questions, name='popular_questions'),
    url(r'^new', views.test, name='test'),
    url(r'^question/(?P<question_id>\d+)/$', views.question_details, name='question_details'),
    url(r'^', views.questions_all, name='questions_all'),

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
