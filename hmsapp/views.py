
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .models import Student
from django.contrib.auth import logout
from .models import Student
# Create your views here.


def home(request):
    studs = Student.objects.all()
    return render(request, 'home.html', {'studs': studs})



# Create your views here.


def login(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']

         user = auth.authenticate(username = username, password = password)
         if user is not None:
             auth.login(request, user)
             return redirect("/home")
         else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login') 
    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        together_name = first_name + " " + last_name
        if password == re_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                o_ref = Student(name=together_name, enrollment=username, email=email, temperature=0, oxygen=0)
                o_ref.save()
                messages.info(request, 'User Created..')
                return redirect("/")
        else:
            messages.info(request, 'Password Not Matching..')

        return render(request,'register.html')
    else:
        return render(request, 'register.html')


def logout(request):
    logout(request)
    return redirect("/")

def forgetpass(request):
    return render(request, 'forgetpassword.html')