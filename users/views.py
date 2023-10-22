from django.shortcuts import render,redirect
from .forms import Registerform
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    form=Registerform
    if request.method=='POST':
        form=Registerform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created successfully for {username}')
            return redirect('signin')
    context={
        'forms':form
    }
    return render(request,'users/register.html',context)



def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,f'{username} Welcome to AGRITECH')
            return redirect('home')
        else:
            messages.warning(request,'You have entered wrong credentials')
            return redirect('signin')
        
    return render(request,'users/login.html')


def home(request):
    return render(request,'users/home.html')


def Logout(request):
    logout(request)
    messages.warning(request,'You have been logged out')
    return redirect('signin')