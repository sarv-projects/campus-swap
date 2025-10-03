from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
def signup_view(request):
    if request.method == "POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully!!Please log in .")
            return redirect("login")
    else:
        form=CustomUserCreationForm
    return render(request,'users/signup.html',{'form':form})


# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    """
    Dashboard for logged-in users.
    Shows links to:
    - Browse items
    - Sell item
    - My orders/listings
    """
    user = request.user
    return render(request, 'users/dashboard.html', {'user': user})
