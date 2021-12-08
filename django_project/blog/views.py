from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post

@login_required
def home(request):
    return render(request, "blog/home.html", {
        "title": "HOME", "posts": Post.objects.all()
        })

@login_required
def about(request):
    return render(request, "blog/about.html")

