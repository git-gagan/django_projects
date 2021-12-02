from django.shortcuts import render

posts = [
    {
        "title" : "Django",
        "author": "Gagan",
        "content" : "This is first post related to django",
        "date_posted" : "December"
    },
    {
        "title" : "Flask",
        "author" : "Bunny",
        "content" : "I have done flask before",
        "date_posted" : "January"
    }
]

def home(request):
    return render(request, "blog/home.html", {"title":"HOME", "posts":posts})

def about(request):
    return render(request, "blog/about.html")
