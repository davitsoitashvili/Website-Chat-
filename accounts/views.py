from django.shortcuts import render,redirect
from accounts.forms import RegisterForm
from accounts.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def signUpVIew(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main page")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'registeform':form})


def signInView(request):
    if request.POST:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("main page")
    else:
        form = AuthenticationForm()



    return render(request, 'login.html', {"loginform":form})
