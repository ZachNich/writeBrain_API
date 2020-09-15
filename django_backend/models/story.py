from django.db import models
from django.contrib.auth.models import User

class Story(models.Model):

    title = models.CharField()
    description = models.CharField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Story")
        verbose_name_plural = ("Stories")