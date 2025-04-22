from django.db import models
from django.conf import settings

class Content(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)
    token = models.CharField(max_length=20)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)


