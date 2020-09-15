from django.db import models

class Mood(models.Model):

    name = models.CharField(max_length=16)

    class Meta:
        verbose_name = ("Mood")
        verbose_name_plural = ("Moods")