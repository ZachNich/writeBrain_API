from django.contrib.auth.models import User
from rest_framework import viewsets

class Users(viewsets.ModelViewSet):
    queryset = User.objects.all()