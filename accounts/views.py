from django.shortcuts import render
from .models import User

from .forms import LoginForm
from django.contrib.auth import authenticate, login , logout
# Create your views here.

def user_login(request):

    if request.user.is_authenticated:

        return redirect("home")

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():
            
            cd = form.cleaned_data

            user = authenticate(request , username = username , password = password)

            if user is not None:

                login(request, user)

    return render(request, 'login.html', context= {'form' : form}) 



def user_logout(request):
    logout(request)