from django.conf.urls import patterns, url

from qa import views

urlpatterns = patterns('',
    url(r'^$', views.test, name='test'),
    url(r'^login', views.test, name='test'),
    url(r'^ask', views.test, name='test'),
    url(r'^signup', views.test, name='test'),
    url(r'^popular', views.test, name='test'),
    url(r'^new', views.test, name='test'),
    url(r'^question/(?P<question_id>\d+)/$', views.test, name='test'),
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
