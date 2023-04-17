from django.db import models
from django.conf import settings

class Posting(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

class Reply(models.Model):
    content = models.CharField(max_length=200)
    posting = models.ForeignKey(Posting, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)