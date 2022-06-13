from django.shortcuts import render
from .models import Team
from cars.models import Car
from django.db.models import Min,Max
# Create your views here.
def home(request):
    search_data = {}
    team = Team.objects.all()
    search_data['model'] = Car.objects.all().values_list('model',flat=True).distinct()
    search_data['city'] = Car.objects.all().values_list('city',flat=True).distinct()
    search_data['year'] = Car.objects.all().values_list('year',flat=True).distinct()
    search_data['body_style'] = Car.objects.all().values_list('body_style',flat=True).distinct()
    featured_car = Car.objects.order_by('-created_date').filter(is_featured=True)
    min_value = Car.objects.all().aggregate(Min('price'))
    mval = Car.objects.all().aggregate(Max('price'))
    all_car = Car.objects.order_by('-created_date')
    return render(request,'pages/index.html',{
        'teams':team,
        'fcar':featured_car,
        'car':all_car,
        'sdata':search_data,
        'max':mval,
        'min':min_value,
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