from django.shortcuts import redirect, render
from .models import Car
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Inquiry
from django.db.models import Min,Max
# Create your views here.
def cars(request):
    sdata = {}
    sdata['model'] = Car.objects.values_list('model',flat=True).distinct()
    sdata['city'] = Car.objects.values_list('city',flat=True).distinct()
    sdata['year'] = Car.objects.values_list('year',flat=True).distinct()
    maxval = Car.objects.aggregate(Max('price'))
    car = Car.objects.order_by('-created_date')
    paginator = Paginator(car,4)
    pg = request.GET.get('page')
    paged_cars = paginator.get_page(pg)
    return render(request,'cars/carhome.html',{
        'car':paged_cars,
        'sdata':sdata,
        'max':maxval
    })

def car_detail(request,id):
    userr = None
    #if User:
    #    if User.is_authenticated:
    #        userr = User.objects.get(username=request.user)
    car_data = Car.objects.get(id=id)
    return render(request,'cars/car_detail.html',{
        'data' : car_data,
        'userr':userr,
    })

def search(request):
    cars = Car.objects.order_by('-created_date')
    sdata = {}
    sdata['model'] = Car.objects.values_list('model',flat=True).distinct()
    sdata['year'] = Car.objects.values_list('year',flat=True).distinct()
    sdata['color'] = Car.objects.values_list('color',flat=True).distinct()
    sdata['city'] = Car.objects.values_list('city',flat=True).distinct()
    sdata['body_style'] = Car.objects.values_list('body_style',flat=True).distinct()
    sdata['doors'] = Car.objects.values_list('doors',flat=True).distinct()
    maxval = Car.objects.aggregate(Max('price'))
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(car_title__icontains=keyword)
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if keyword:
            cars = cars.filter(body_style__iexact=body_style)
    if 'max_price' in request.GET or 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        cars = cars.filter(price__gte=min_price,price__lte=max_price)
        
    return render(request,'cars/search.html',{
        'car':cars,
        'sdata':sdata,
        'maxval':maxval
    })


def inquiry(request):
    if request.method == "POST":
        inquiry = Inquiry()
        inquiry.first_name = request.POST['first_name']
        inquiry.last_name = request.POST['last_name']
        car_id = Car.objects.get(pk=request.POST['car'])
        inquiry.car = car_id
        inquiry.user = request.user
        inquiry.city = request.POST['city']
        inquiry.state = request.POST['state']
        inquiry.email = request.POST['email']
        inquiry.phone = request.POST['phone']
        inquiry.comments = request.POST['message']
        inquiry.save()

    return redirect('dashboard-page')