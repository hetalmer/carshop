from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from cars.models import Inquiry
# Create your views here.
x = None
def dashboard(request):
    data = Inquiry.objects.filter(user=request.user.id).all()
    return render(request,'accounts/dashboard.html',{
        'ddata':data
    })

def login1(request):
    global x 
    if request.method == 'GET':
        x = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user1 = auth.authenticate(request,username=username,password=password)
        if user1 is not None:
            auth.login(request,user1)
            messages.error(request,'You are successfully logged in')
            if x is not None:
                return redirect(x)
            else:
                return redirect('dashboard-page')
        else:
            messages.error(request,'email or Password is not valid')
            return redirect('login-page')
    else:
        return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if password == request.POST['confirm_password']:
            if User.objects.filter(username=username).exists():
                messages.error(request,'User name already exist')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                user.save()
                auth.login(request,user)
                messages.error(request,'You are sucessfully logged in')
                return redirect('dashboard-page')
        else:
            messages.error(request,'Password and Confirm Password does not match')
        return redirect('register-page')
    else:
        return render(request,'accounts/register.html')


def logout1(request):
    auth.logout(request)
    return redirect('home-page')

def ddelete(request,id):
    dash = Inquiry.objects.filter(pk=id)
    dash.delete()
    return redirect('dashboard-page')