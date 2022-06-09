from django.shortcuts import render
from .models import Team
# Create your views here.
def home(request):
    team = Team.objects.all()
    return render(request,'pages/index.html',{
        'teams':team
    })

def contact(request):
    return render(request,'pages/contact.html')

def about(request):
    team = Team.objects.all()
    return render(request,'pages/about.html',{
        'teams':team
    })

def services(request):
    return render(request,'pages/services.html')