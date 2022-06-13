from django.shortcuts import render
from .models import Car
from django.core.paginator import Paginator
# Create your views here.
def cars(request):
    car = Car.objects.order_by('-created_date')
    paginator = Paginator(car,4)
    pg = request.GET.get('page')
    paged_cars = paginator.get_page(pg)
    return render(request,'cars/carhome.html',{
        'car':paged_cars
    })

def car_detail(request,id):
    car_data = Car.objects.get(id=id)
    return render(request,'cars/car_detail.html',{
        'data' : car_data
    })

def search(request):
    cars = Car.objects.order_by('-created_date')
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
        'car':cars
    })
