from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField('description')
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField()
    asked_by = models.OneToOneField(User, null=True)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title[:70]

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    is_best = models.BooleanField('is best answer?')
    submitted_by = models.OneToOneField(User)

    def __unicode__(self):
        return self.answer[:70]

class Tag(models.Model):
    title = models.CharField(max_length=50)
    question = models.ManyToManyField(Question)

    def __unicode__(self):
        return self.title
