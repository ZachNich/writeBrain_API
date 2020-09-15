from django.db import models
from django.contrib.auth.models import User
from .mood import Mood
from .story import Story

class Sprint(models.Model):

    body = models.CharField(max_length=500000)
    started_at = models.DateTimeField(auto_now=True)
    ended_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    story = models.OneToOneField(Story, on_delete=models.CASCADE)
    mood_before = models.ForeignKey(Mood, related_name="mood_before", on_delete=models.DO_NOTHING)
    mood_after = models.ForeignKey(Mood, related_name="mood_after", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("Sprint")
        verbose_name_plural = ("Sprints")