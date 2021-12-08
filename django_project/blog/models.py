from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    """
    This will create a DB table for posts and has a manytoone relationship with User
    """
    title = models.CharField(max_length=40)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
