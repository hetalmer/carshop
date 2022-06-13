from django.urls import path
from . import views
urlpatterns = [
    path('',views.cars,name='cars-home'),
    path('<int:id>',views.car_detail,name='car-detail-page'),
    path('search',views.search,name='search-page')
]
