from django.shortcuts import redirect, render
from .forms import MyForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            messages.success(request, f"Account created for user {username}")
            return redirect("blog-home")
    else:
        form = MyForm()
    return render(request, "users/register.html", {"form":form})
