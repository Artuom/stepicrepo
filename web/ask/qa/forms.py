from django import forms
from models import Question, Answer
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    author = forms.IntegerField(widget=forms.HiddenInput())
    """def clean_text(self):
        print "in clean data"
        #text = self.cleaned_data['text']
        #print "txt = ", text"""
    def save(self):
        id = int(self.cleaned_data['author'])
        self.cleaned_data['author'] = User.objects.filter(id = id)[0]
        question = Question(**self.cleaned_data)

        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())
    #author = forms.IntegerField(widget=forms.HiddenInput())
    author = forms.IntegerField(widget=forms.HiddenInput())
    """def clean_text(self):
        text = self.cleaned_data['text']"""

    def save(self):
        print "cleaned_data====", self.cleaned_data
        id = int(self.cleaned_data['question'])
        self.cleaned_data['question'] = Question.objects.filter(id = id)[0]
        id = int(self.cleaned_data['author'])
        self.cleaned_data['author'] = User.objects.filter(id = id)[0]
        answer = Answer(**self.cleaned_data)
        #answer.author
        #answer.author = User.objects.filter(id=1)[0]
        answer.save()
        return answer

class RegistrationForm(forms.Form):
    def __init__(self):
        self.username = forms.CharField(length=30, maxlength=30,
                                is_required=True, validators=[validators.RegexValidator(r'^[0-9a-zA-Z]*$',
                                message='Only alphanumericcharacters are allowed.', code='invalid_username'),
                                self.isValidUsername])
        self.email = forms.EmailField(is_requiered=True, validators = [validators.validate_email])
        self.password1 = forms.PasswordField(is_requiered = True)
        self.password2 = forms.PasswordField(is_requiered = True, validators = [validators.AlwaysMatchesOtherField('password1', 'Passwords must match.')])


    def isValidUsername(self, field_data, all_data):
        try:
            User.objects.get(username=field_data)
        except User.DoesNotExist:
            return
        raise ValidationError('The username "%s" is already taken.' % field_data)

    def save(self, new_data):
        u = User.objects.create_user(new_data['username'],
                                     new_data['email'],
                                     new_data['password1'])
        u.is_active = False
        u.save()
        return u


"""class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.PasswordField()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).count() > 0:
            raise forms.ValidationError, "%s already exists" % username
        return username"""

class Register(UserCreationForm):
    password = forms.CharField(label=("Password"),
        strip=False,
        widget=forms.PasswordInput)
    password1=None
    password2=None

    def clean_password2(self):
        print "in clean_password2"
        self.password = password
        return self.password

    def save(self):
        print "cleaned_data====", self.cleaned_data
        #user = super(UserCreationForm, self).save(commit=False)
        user = User(**self.cleaned_data)
        print user
        password = str(self.cleaned_data['password'])
        user.set_password(password)
        user.save()
        return user
