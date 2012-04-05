from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    questions_number = models.IntegerField(default=0)
    answers_number = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.user.username
