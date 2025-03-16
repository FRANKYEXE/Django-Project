from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("welcome , you are logged in") 

def signup_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    context = {}
    if request.method=='POST':
        un = request.POST.get('un','')
        email = request.POST.get('em')
        pw1 = request.POST.get('pw1')
        pw2 = request.POST.get('pw2')
        if pw1 == pw2:
            if User.objects.filter(username=un):
                context['error']= 'Username already Exists!!'
            else:
                User.objects.create_user(
                    username=un,
                    email=email,
                    password=pw1,
                )
                return redirect('login')            
        else:
            context['error']= 'Password does not match'
    return render(request,'signup.html',context)



def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    context = {}
    if request.method=='POST':
        un = request.POST.get('un','')
        pw = request.POST.get('pw','')
        user = authenticate(request,username=un,password=pw)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            context['error']= 'Invalid Credentials'
        
    return render(request,'login.html',context)
  
def logout_user(request):
    logout(request)
    return redirect('login')

