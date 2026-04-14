from django.shortcuts import render , redirect
from .models import User

from .forms import LoginForm
from django.contrib.auth import authenticate, login , logout
# Create your views here.

def user_login(request):

    if request.user.is_authenticated:

        return redirect("post_list")
    
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():
             username = form.cleaned_data.get('username')
             password = form.cleaned_data.get("password")
             user = authenticate(request, username=username, password=password)
     
             if user is not None:

                    login(request, user)
                    return redirect("post_list") 
            
             else:
               
                form.add_error(None, "username or password is incorrect")
              
    return render(request, 'login.html', context= {'form' : form}) 



def user_logout(request):
    logout(request)