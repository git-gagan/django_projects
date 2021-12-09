from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import MyForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            messages.success(request, f"Account created for user {username}")
            return redirect("login")
    else:
        form = MyForm()
    return render(request, "users/register.html", {"form":form})

@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Profile updated for user {request.user.username}")
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        "u_form": user_form,
        "p_form": profile_form
    }
    
    return render(request, "users/profile.html", context)