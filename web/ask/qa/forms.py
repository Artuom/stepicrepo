from django import forms
from models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    """def clean_text(self):
        print "in clean data"
        #text = self.cleaned_data['text']
        #print "txt = ", text"""
    def save(self):
        question = Question(**self.cleaned_data)
        question.author = User.objects.filter(id=1)[0]
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.CharField(widget=forms.HiddenInput())
    """def clean_text(self):
        text = self.cleaned_data['text']"""

    def save(self):
        id = int(self.cleaned_data['question'])
        self.cleaned_data['question'] = Question.objects.filter(id = id)[0]
        answer = Answer(**self.cleaned_data)
        answer.author = User.objects.filter(id=1)[0]
        answer.save()
        return answer
