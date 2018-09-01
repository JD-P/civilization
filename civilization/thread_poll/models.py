from django.db import models
from django.contrib.auth.models import User

class ThreadPoll(models.Model):
    thread = models.ForeignKey('civforum.Thread', on_delete=models.CASCADE)
    
    
class ThreadPollOption(models.Model):
    poll = models.ForeignKey('ThreadPoll', on_delete=models.CASCADE)
    label = models.CharField(max_length=200)
    description = models.TextField()
    
class ThreadPollChoice(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    option = models.ForeignKey('ThreadPollOption', on_delete=models.CASCADE)
    date_chosen = models.DateTimeField()
    
class ThreadPollACL(models.Model):
    poll = models.ForeignKey('ThreadPoll', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_type = models.ForeignKey('ThreadPollAT', on_delete=models.CASCADE)

class ThreadPollAT(models.Model):
    label = models.CharField(max_length=50)
    description = models.TextField()
