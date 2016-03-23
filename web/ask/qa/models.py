from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=1)
    author = models.ForeignKey(User)
    likes = User()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return '/question/%d' % self.pk
    class Meta:
        db_table = 'blogposts'
        ordering = ['-added_at']

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=True,
        on_delete = models.DO_NOTHING)
    author = models.ForeignKey(User, default=1)
    def __str__(self):
        return self.text
    def get_absolute_url(self):
        return '/question/%d/' % self.question.id

class Session(models.Model):
    key = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User)
    expires = models.DateTimeField()
