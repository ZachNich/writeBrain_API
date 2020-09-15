from django.db import models
from django.contrib.auth.models import User
from .mood import Mood

class Story(models.Model):

    body = models.CharField()
    started_at = models.DateTimeField(auto_now=True)
    ended_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mood_before = models.ForeignKey(Mood, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("Story")
        verbose_name_plural = ("Stories")