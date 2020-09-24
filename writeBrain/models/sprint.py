from django.db import models
from django.contrib.auth.models import User
from .mood import Mood
from .story import Story

class Sprint(models.Model):

    body = models.CharField(max_length=500000)
    started_at = models.DateTimeField(auto_now=False)
    ended_at = models.DateTimeField(auto_now=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    mood_before = models.ForeignKey(Mood, related_name="sprint_before", on_delete=models.DO_NOTHING)
    mood_after = models.ForeignKey(Mood, related_name="sprint_after", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("sprint")
        verbose_name_plural = ("sprints")