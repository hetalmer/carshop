from email import message
from django.contrib import messages
from django.shortcuts import render
from .models import Team
from cars.models import Car
from django.db.models import Min,Max
from django.core.mail import send_mail
import folium as folium
import geocoder as geocoder
# Create your views here.
def home(request):
    search_data = {}
    team = Team.objects.all()
    search_data['model'] = Car.objects.values_list('model',flat=True).distinct()
    search_data['city'] = Car.objects.values_list('city',flat=True).distinct()
    search_data['year'] = Car.objects.values_list('year',flat=True).distinct()
    search_data['body_style'] = Car.objects.values_list('body_style',flat=True).distinct()
    featured_car = Car.objects.order_by('-created_date').filter(is_featured=True)
    min_value = Car.objects.all().aggregate(Min('price'))
    mval = Car.objects.all().aggregate(Max('price'))
    all_car = Car.objects.order_by('-created_date')[:6]
    return render(request,'pages/index.html',{
        'teams':team,
        'fcar':featured_car,
        'car':all_car,
        'sdata':search_data,
        'max':mval,
        'min':min_value,
    })

def contact(request):
    if request.method == 'POST':
        send_mail(
            request.POST['subject'],
            request.POST['message'],
            'hetalmer5886@gmail.com',
            ('hetalmer5886@gmail.com',),
            fail_silently=False,
        )
        messages.error(request,'Mail sent successfully')
    return render(request,'pages/contact.html')

def about(request):
    team = Team.objects.all()
    return render(request,'pages/about.html',{
        'teams':team
    })

def services(request):
    return render(request,'pages/services.html')

def mapview(request,city):
    #get map
    location = geocoder.osm(city)
    country = location.country
    location1 = geocoder.osm(country)
    
    m = folium.Map(location=[location1.lat,location1.lng],zoom_start=5)
    folium.Marker([location.lat,location.lng],tooltip="Click for more",
    popup=country+","+city).add_to(m)
    #get map in html format
    m = m._repr_html_()
    context = {
        'm':m,
    }
    return render(request,'pages/viewmap.html',context)