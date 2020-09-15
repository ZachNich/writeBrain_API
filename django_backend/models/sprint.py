from django.db import models
from django.contrib.auth.models import User
from .mood import Mood

class Sprint(models.Model):

    body = models.CharField()
    started_at = models.DateTimeField(auto_now=True)
    ended_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mood_before = models.ForeignKey(Mood, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("Sprint")
        verbose_name_plural = ("Sprints")