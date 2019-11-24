from django.shortcuts import render,redirect
from pages.models import Message
from pages.forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required(login_url="login page")
def mainView(request):
    User = f"სახელი: {request.user.first_name} გვარი:{request.user.last_name}"
    messages = Message.objects.all()
    form = MessageForm()
    if request.POST:
        form = MessageForm(request.POST)
        message = form['message'].value()
        Message(author=request.user.first_name, message=message).save()


    return render(request, 'main.html', {'messages':messages,'form':form,"userinfo":User})


@login_required(login_url="login page")
def logoutView(request):
    if request.GET:
        logout(request)
        return redirect('login page')

    return render(request, 'main.html', {})

