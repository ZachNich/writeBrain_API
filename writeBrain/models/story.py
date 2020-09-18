from django.db import models
from django.contrib.auth.models import User

class Story(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Story")
        verbose_name_plural = ("Stories")